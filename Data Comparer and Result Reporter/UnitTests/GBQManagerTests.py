import unittest

from DatabaseConfiguration import *
from Utils.DataIO import *
from SQL.GBQConnector import *
from SQL.GBQManager import *
from google.cloud import bigquery

class GBQManagerTests(unittest.TestCase):
    def setUp(self):
        self.gbqConnector = GBQConnector(GBQCredentials, Project, LaunchBrowser)
        self.gbqClient = self.gbqConnector.connectToDatabase()

    def tearDown(self):
        ""

    def test_GBQManager_GetRowsFromTable(self):
        gbqManager = GBQManager(self.gbqClient)
        targetTableData = gbqManager.getAllRowsFromTable("Person_UCH_CDW_20170620111203696_19000101000000000_20170620111203696")

        self.assertTrue(True)

    def test_GBQManager_GetRowCountFromTable(self):
        gbqManager = GBQManager(self.gbqClient)
        targetTableNameandCount = gbqManager.getFullTableRowCount("Person_UCH_CDW_20170620111203696_19000101000000000_20170620111203696")

        self.assertTrue(True)

    def test_GBQManager_GetRowCountFromDataset(self):
        targetTables = DataIO.readData(targetFullFile)

        gbqManager = GBQManager(self.gbqClient)
        targetTableNameandCount = gbqManager.getFullDatasetTableNameAndRowCount(targetTables)

        for table in targetTableNameandCount:
            print(table.TableName + " : " + str(table.TableCount))

        self.assertTrue(True)

    def test_GBQManager_GetSchema(self):
        datasetSchema = []
        targetTables = DataIO.readData(targetFullFile)

        for table in targetTables:
            gbqManager = GBQManager(self.gbqClient)
            tableSchema = gbqManager.getSchema(table)
            datasetSchema.append(tableSchema)

        for table in datasetSchema:
            print('\n')
            print(table.TableName)

            for columnSchema in table.ColumnSchemaList:
                print(columnSchema.Name + " : " + columnSchema.DataType)


    def test_GBQManager_GetSampleData(self):
        targetDatasetSampleData = []
        targetTables = DataIO.readData(targetFullFile)

        for tableId in range(len(targetTables)):
            gbqManager = GBQManager(self.gbqClient)
            targetTableSampleData = gbqManager.getSampleTableData(targetTables[tableId])
            targetDatasetSampleData.append(targetTableSampleData)

        for targetTable in targetDatasetSampleData:
            print(targetTable.TableName)
            for targetRow in range(len(targetTable.SampleData)):
                for targetColumn in range(len(targetTable.SampleData[0])):
                    print(targetTable.SampleData[targetRow][targetColumn])


        self.assertTrue(True)

    # ***************** private methods **********************
