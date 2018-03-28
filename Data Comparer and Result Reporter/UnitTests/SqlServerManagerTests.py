import unittest

from Configuration import *
from SQL.SqlServerConnector import *
from SQL.SqlServerManager import *
from Utils.DataIO import *

class DBManagerTests(unittest.TestCase):
    def setUp(self):
        sqlServerConnector = SqlServerConnector(Driver, Server, Database, UID, PWD)
        self.cursor = sqlServerConnector.connectToDatabase()

    def tearDown(self):
        ""

    def test_SqlServerManager_CreateSqlStatementForAllSourceTables(self):
        sqlServerManager = SqlServerManager(self.cursor)
        sqlServerManager.getAllTablesSqlStatement()
        cursor = sqlServerManager.getCursor()

        for row in cursor:
            print(row[0])

        self.assertTrue(True)

    def test_SqlServerManager_GetAllRowsFromTable(self):
        sqlServerManager = SqlServerManager(self.cursor)
        sqlServerManager.getAllRowsFromTable("Person")
        cursor = sqlServerManager.getCursor()

        for row in cursor:
            print(row)

        self.assertTrue(True)


    def test_SqlServerManager_GetTableRowCount(self):
        sqlServerManager = SqlServerManager(self.cursor)
        sqlServerManager.getFullTableRowCount("Person")
        cursor = sqlServerManager.getCursor()

        for row in cursor:
            print(row[0])

        self.assertTrue(True)

    def test_SqlServerManager_GetDatasetRowCounts(self):
        sourceTables = DataIO.readData(sourceFullFile)

        sqlServerManager = SqlServerManager(self.cursor)
        tableNamesAndCounts = sqlServerManager.getFullDatasetTableNameAndRowCount(sourceTables)

        for table in tableNamesAndCounts:
            print(table.TableName + " : " + str(table.TableCount))

        self.assertTrue(True)

    def test_SqlServerManager_GetSchema(self):
        datasetSchema = []
        sourceTables = DataIO.readData(sourceFullFile)

        for table in sourceTables:
            sqlServerManager = SqlServerManager(self.cursor)
            tableSchema = sqlServerManager.getSchema(table)
            datasetSchema.append(tableSchema)

        for table in datasetSchema:
            print('\n')
            print(table.TableName)

            for columnSchema in table.ColumnSchemaList:
                print(columnSchema.Name + " : " + columnSchema.DataType)

        self.assertTrue(True)

    def test_SqlServerManager_GetSampleData(self):
        mockTargetUIds = [1, 2, 3, 4, 5]

        sourceDatasetSampleData = []
        sourceTables = DataIO.readData(sourceFullFile)
        targetUKeys = DataIO.readIDData(targetUKeyFile)

        for tableId in range(len(sourceTables)):
            sqlServerManager = SqlServerManager(self.cursor)
            sourceTableSampleData = sqlServerManager.getSampleTableData(sourceTables[tableId], targetUKeys[sourceTables[tableId]], mockTargetUIds)
            sourceDatasetSampleData.append(sourceTableSampleData)

        for sourceTable in sourceDatasetSampleData:
            print(sourceTable.TableName)
            for sourceRow in range(len(sourceTable.SampleData)):
                for sourceColumn in range(len(sourceTable.SampleData[0])):
                    print(sourceTable.SampleData[sourceRow][sourceColumn])

        self.assertTrue(True)

    def test_SqlServerManager_GetIncrementalTableNameandCount(self):
        """
        sqlServerManager = SqlServerManager(self.cursor)
        sqlServerManager.getIncrementalTableRowCount("Person_UCH_CDW_20170620111203696_19000101000000000_20170620111203696","Id")
        cursor = sqlServerManager.getCursor()

        for row in cursor:
            print(row)
        """

        table = "Person_UCH_CDW_20170620111203696_19000101000000000_20170620111203696"

        tableName, start, end = DateParser.getDates(table)
        incrementalSqlStatement = SqlStatementManager.SqlServer.getIncrementalTableRowCount(tableName, "yo", start, end)

        print(incrementalSqlStatement)



        self.assertTrue(True)
