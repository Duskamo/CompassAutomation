
from DatabaseConfiguration import *
from SQL.SqlStatementManager import *
from Models.SQLTestResult import *
from Models.ColumnSchema import *
from Models.TableSchema import *
from Models.TableSampleData import *
from Utils.DataHandler import *
from Utils.DateParser import *

class SqlServerManager:
    def __init__(self,cursor):
        self.cursor = cursor

    def getAllRowsFromTable(self,table):
        self.cursor.execute(SqlStatementManager.SqlServer.getAllRowsFromTable(table))

    def getAllTablesSqlStatement(self):
        self.cursor.execute(SqlStatementManager.SqlServer.useDatabase(Database))
        self.cursor.execute(SqlStatementManager.SqlServer.generateRowCountQueriesForAllTables())

    def getFullTableRowCount(self,table):
        self.cursor.execute(SqlStatementManager.SqlServer.getFullTableRowCount(table))

    def getFullDatasetTableNameAndRowCount(self,dataset):
        tableNamesAndCounts = []

        self.cursor.execute(SqlStatementManager.SqlServer.useDatabase(Database))

        for table in dataset:
            self.cursor.execute(SqlStatementManager.SqlServer.getFullTableRowCount(table))

            for row in self.cursor.fetchall():
                tableNamesAndCounts.append(SQLTestResult(table,row.Count))

        return tableNamesAndCounts

    def getIncrementalTableRowCount(self,table, uid):
        tableName, start, end = DateParser.getDates(table)

        self.cursor.execute(SqlStatementManager.SqlServer.getIncrementalTableRowCount(tableName,uid,start,end))

    def getIncrementalDatasetTableNameAndRowCount(self,dataset):
        tableNamesAndCounts = []

        self.cursor.execute(SqlStatementManager.SqlServer.useDatabase(Database))

        for table in dataset:
            self.cursor.execute(SqlStatementManager.SqlServer.getFullTableRowCount(table))

            for row in self.cursor.fetchall():
                tableNamesAndCounts.append(SQLTestResult(table,row.Count))

        return tableNamesAndCounts

    def getSchema(self,table):
        columnSchema = []

        self.cursor.execute(SqlStatementManager.SqlServer.getSchemaForTable(table))

        for row in self.cursor:
            columnSchema.append(ColumnSchema(row[0],row[1]))

        return TableSchema(table,columnSchema)

    def getSampleTableData(self,table,ukey,uids):
        uidsString = DataHandler.ListToCommaString(uids)

        self.cursor.execute(SqlStatementManager.SqlServer.getSampleTableData(table,ukey,uidsString))

        cursorList = list(self.cursor)

        sampleData = [[0 for x in range(len(cursorList[0]))] for y in range(len(cursorList))]


        for rowId in range(len(cursorList)):
            for colId in range(len(cursorList[0])):
                sampleData[rowId][colId] = cursorList[rowId][colId]

        return TableSampleData(table,sampleData)

    def getRows(self,table,uid,uids):
        sql = 'select * from {} (readuncommited) '\
			  'where {} in ({}) order by {}'
        sql.format(table,uid,uids,uid)

    def getCursor(self):
        return self.cursor


  