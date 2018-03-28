import unittest
import xlwt
from SQL.GBQConnector import *
from SQL.GBQManager import *
from SQL.SqlServerConnector import *
from SQL.SqlServerManager import *
from Utils.DataIO import *

class CSVFileIOTests(unittest.TestCase):
    def setUp(self):
        ""

    def tearDown(self):
        ""

    def test_readInAllInputLists(self):
        sourceFullData = DataIO.readData(sourceFullFile)
        sourceIncData = DataIO.readData(sourceIncFile)
        targetFullData = DataIO.readData(targetFullFile)
        targetIncData = DataIO.readData(targetIncFile)

        print("\n****************************************Source Full Data****************************************\n")
        for table in sourceFullData:
            print(table)

        print("\n****************************************Source Inc Data****************************************\n")
        for table in sourceIncData:
            print(table)

        print("\n****************************************Target Full Data****************************************\n")
        for table in targetFullData:
            print(table)

        print("\n****************************************Target Inc Data****************************************\n")
        for table in targetIncData:
            print(table)

    def test_OutputDataToDirectory(self):
        # Get source and target tables to test from input files
        self.sourceTables = DataIO.readData(sourceFullFile)
        self.targetTables = DataIO.readData(targetFullFile)
        targetUKeys = DataIO.readIDData(targetUKeyFile)

        # Connect to both databases
        self.sqlServerConnector = SqlServerConnector(Driver, Server, Database, UID, PWD)
        self.SqlServerCursor = self.sqlServerConnector.connectToDatabase()

        self.gbqConnector = GBQConnector(GBQCredentials, Project, LaunchBrowser)
        self.gbqClient = self.gbqConnector.connectToDatabase()

        sqlServerManager = SqlServerManager(self.SqlServerCursor)
        gbqManager = GBQManager(self.gbqClient)

        # Get schema and sample data information from databases
        for tableId in range(len(self.sourceTables)):
            # Grab source and target schema info
            sourceTableSchema = sqlServerManager.getSchema(self.sourceTables[tableId])
            targetTableSchema = gbqManager.getSchema(self.targetTables[tableId])

            # Grab source and target data validation info
            targetTableSampleData = gbqManager.getSampleTableData(self.targetTables[tableId])
            uIDsList = DataHandler.getUIDsFromTargetTable(targetTableSampleData)
            sourceTableSampleData = sqlServerManager.getSampleTableData(self.sourceTables[tableId], targetUKeys[self.sourceTables[tableId]], uIDsList)

            # Write schema to excel sheet
            self.__writeToExcel(self.sourceTables[tableId], sourceTableSchema.ColumnSchemaList, targetTableSchema.ColumnSchemaList, 'Schema')

            # Write Data Validation to excel sheet
            self.__writeToExcel(self.sourceTables[tableId], sourceTableSampleData.SampleData, targetTableSampleData.SampleData, 'Sample Data')

    def __writeToExcel(self,tabName,sourceList,targetList,type):
        book = xlwt.Workbook()
        target  = book.add_sheet('target')
        source = book.add_sheet('source')

        if type == "Schema":
            columnCount = len(sourceList)

            for columnId in range(columnCount):
                target.write(0, columnId, targetList[columnId].Name)
                target.write(1, columnId, targetList[columnId].DataType)
                source.write(0, columnId, sourceList[columnId].Name)
                source.write(1, columnId, sourceList[columnId].DataType)
        elif type == "Sample Data":
            rowNum = len(sourceList)

            for i in range(rowNum):
                colNum = len(sourceList[i])
                for j in range(colNum):
                    target.write(i, j, targetList[i][j])
                    source.write(i, j, sourceList[i][j])

        path = TestOutputDirectory + "\\" + type + "\\" + tabName + ".xls"
        book.save(path)