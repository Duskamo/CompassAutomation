from google.cloud import bigquery
import uuid
import time

from DatabaseConfiguration import *
from Utils.DataHandler import *
from Models.ColumnSchema import *
from Models.TableSchema import *
from Models.SQLTestResult import *
from Models.TableSampleData import *
from SQL.SqlStatementManager import *

class GBQManager:

	def __init__(self,client):
		self.client = client

	def getAllRowsFromTable(self, table):
		self.__run_query(Project, SqlStatementManager.GoogleBigQuery.getAllRowsFromTable(table))

	def getFullTableRowCount(self,table):
		self.__run_query(Project, SqlStatementManager.GoogleBigQuery.getFullTableRowCount(table))

	def getFullDatasetTableNameAndRowCount(self,tableList):
		targetTablesString = DataHandler.ListToQuotedCommaString(tableList)

		rows = self.__run_query(Project, SqlStatementManager.GoogleBigQuery.getFullDatasetTableNameAndRowCount(targetTablesString))

		tableNameAndCountList = []

		for row in rows:
			tableNameAndCountList.append(SQLTestResult(row[0],row[1]))

		return tableNameAndCountList

	def getSchema(self,tableName):
		dataset = self.client.dataset(Dataset)
		table = dataset.table(tableName)

		table.reload()

		schemaList =[]

		for field in table.schema:
			schemaList.append(ColumnSchema(field.name,field.field_type))

		return TableSchema(tableName,schemaList)

	def getSampleTableData(self, table):
		rows = self.__run_query(Project, SqlStatementManager.GoogleBigQuery.getSampleTableData(table))

		sampleData = [[0 for x in range(len(rows[0]))] for y in range(len(rows))]

		for rowId in range(len(rows)):
			for colId in range(len(rows[0])):
				sampleData[rowId][colId] = rows[rowId][colId]

		return TableSampleData(table, sampleData)

	# ******************* private methods ********************
	def __wait_for_job(self,job):
		while True:
			job.reload()  # Refreshes the state via a GET request.
			if job.state == 'DONE':
				if job.error_result:
					raise RuntimeError(job.errors)
				return
			time.sleep(1)

	def __run_query(self, project, query):
		query_job = self.client.run_async_query(str(uuid.uuid4()),query)
		query_job.use_legacy_sql = False
		query_job.begin()

		self.__wait_for_job(query_job)

		# Drain the query results by requesting a page at a time.
		query_results = query_job.results()
		page_token = None
		"""
		while True:
			rows, total_rows, page_token = query_results.fetch_data(
				max_results=10,
				page_token=page_token)

			for row in rows:
				print(row)

			if not page_token:
				break
		"""
		rows, total_rows, page_token = query_results.fetch_data(
			max_results=10,
			page_token=page_token)

		return rows