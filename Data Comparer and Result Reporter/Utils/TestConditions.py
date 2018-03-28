
import unittest
import xlsxwriter
from Configuration import *
from DatabaseConfiguration import *
from Utils.DataIO import *
from Utils.DataHandler import *
from SQL.SqlServerConnector import *
from SQL.GBQConnector import *
from DatabaseConfiguration import *

class TestConditions(unittest.TestCase):

    def setUp(self):
        # init
        self.__initialize()

        # Establish connection to source and target databases
        self.__connectToDatabases()

        # Get data from source and Target CSV files
        self.__selectLoadType()

        # Standardize source and target data so that we're only comparing
        # against the tables loaded into GBQ and not the full source table list.
        if cleanseData:
            self.sourceData = DataHandler.cleanSourceData(self.sourceData,self.targetData)

    def tearDown(self):
        # Create specified xml report for rally upload
        self.__createXMLReports()

        # Save information from sample data and schema data validation runs to specified directory.
        self.__saveTestDataToDirectory()

    ############## private operators ##############
    def __initialize(self):
        self.testCases = []
        self.testResults = []
        self.rallyResults = []
        self.rowCountResults = []
        self.sampleDataResults = []
        self.schemaResults = []

        self.sourceDatasetSampleData = []
        self.targetDatasetSampleData = []
        self.sourceDatasetSchema = []
        self.targetDatasetSchema = []

    def __connectToDatabases(self):
        self.sqlServerConnector = SqlServerConnector(Driver,Server,Database,UID,PWD)
        self.SqlServerCursor = self.sqlServerConnector.connectToDatabase()

        self.gbqConnector = GBQConnector(GBQCredentials,Project,LaunchBrowser)
        self.gbqClient = self.gbqConnector.connectToDatabase()

    def __selectLoadType(self):
        if loadType == "Full":
            self.sourceTables = DataIO.readData(sourceFullFile)
            self.targetTables = DataIO.readData(targetFullFile)
        elif loadType == "Incremental":
            self.sourceTables = DataIO.readData(sourceIncFile)
            self.targetTables = DataIO.readData(targetIncFile)
            self.targetIds = DataIO.readIDData(targetUKeyFile)

    def __createXMLReports(self):
        if reportType == "TestCase":
            DataIO.writeDataForTestCases(testCasesOutputFile,self.testCases)
        elif reportType == "TestResult":
            DataIO.writeDataForTestResults(testCasesResultsOutputFile,self.testResults)
        elif reportType == "RallyResult":
            DataIO.writeDataForRowCountRallyResults(rallyResultsOutputFile,self.rallyResults)
        elif reportType == "FullTestCoverage":
            if self.rowCountResults:
                DataIO.writeDataForRowCountRallyResults(rowCountResultsOutputFile, self.rowCountResults)

            if self.sampleDataResults:
                DataIO.writeDataForRallyResults(sampleDataResultsOutputFile, self.sampleDataResults)

            if self.schemaResults:
                DataIO.writeDataForRallyResults(schemaResultsOutputFile, self.schemaResults)

    def __saveTestDataToDirectory(self):
        for tableId in range(len(self.sourceTables)):
            if self.id() == "TestExecution.SchemaValidation.SchemaValidation.test_schemaValidation":
                # Write schema to excel sheet
                self.__writeToExcel(self.sourceTables[tableId], self.sourceDatasetSchema[tableId].ColumnSchemaList, self.targetDatasetSchema[tableId].ColumnSchemaList, 'Schema')
            elif self.id() == "TestExecution.SampleDataValidation.SampleDataValidation.test_sampleDataValidation":
                # Write Data Validation to excel sheet
                self.__writeToExcel(self.sourceTables[tableId], self.sourceDatasetSampleData[tableId].SampleData, self.targetDatasetSampleData[tableId].SampleData, 'Sample Data')

    def __writeToExcel(self,tabName,sourceList,targetList,type):
        book = xlsxwriter.Workbook()
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
            for columnId in range(columnCount):
                target.write(0, columnId, targetList[columnId].Name)
                source.write(0, columnId, sourceList[columnId].Name)

            for i in range(rowNum):
                colNum = len(sourceList[i])
                bound = alphabetBase(colNum)
                formCol = alphabetBase(colNum+1)
                for j in range(colNum):
                    target.write(i+1, j, targetList[i][j])
                    source.write(i+1, j, sourceList[i][j])
                    x= '{{=IF(AND(EXACT(A{0}:{1}{0},source!A{0}:{1}{0})),"pass","fail")}}'.format(i+1,bound)
                    y = '{0}{1}:{0}{1}'.format(formCol,i+1)
                    target.write_array_formula(y,x)
        path = TestOutputDirectory + "\\" + type + "\\" + tabName + "_" + build + ".xls"
        book.save(path)

    def alphabetBase(i):
        d ={}
        for x, y in enumerate(string.ascii_lowercase, 0):
            d[x]= y
        n = 26
        try:
            return(str(d[i]).upper())
        except:
            y =str(d[i%n])
            z = str(d[(i//n)-1])
            return(z.upper() + y.upper())
