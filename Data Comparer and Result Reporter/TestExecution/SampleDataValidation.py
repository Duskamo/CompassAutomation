from Utils.TestConditions import *
from Utils.Compare import *
from Utils.DataHandler import *
from SQL.SqlServerManager import *
from SQL.GBQManager import *
from Models.RallyResultRC import *

class SampleDataValidation(TestConditions):
    def test_sampleDataValidation(self):
        # Verify source table count matches target table count
        self.assertEqual(len(self.sourceTables), len(self.targetTables))

        # Get sample data from source and target databases
        sourceTables = DataIO.readData(sourceFullFile)
        targetTables = DataIO.readData(targetFullFile)
        targetUKeys = DataIO.readIDData(targetUKeyFile)

        for tableId in range(len(sourceTables)):
            gbqManager = GBQManager(self.gbqClient)
            sqlServerManager = SqlServerManager(self.SqlServerCursor)

            targetTableSampleData = gbqManager.getSampleTableData(targetTables[tableId])
            uIDsList = DataHandler.getUIDsFromTargetTable(targetTableSampleData)
            sourceTableSampleData = sqlServerManager.getSampleTableData(sourceTables[tableId],targetUKeys[sourceTables[tableId]],uIDsList)

            self.targetDatasetSampleData.append(targetTableSampleData)
            self.sourceDatasetSampleData.append(sourceTableSampleData)

        # validating actual results of if source and target tables are equal in data
        self.assertEqual(len(self.sourceDatasetSampleData),len(self.targetDatasetSampleData))

        for tableId in range(len(self.sourceDatasetSampleData)): ###### here - iterate through number of tables ######
            rr = RallyResult(self.sourceTables[tableId],self.sourceTables[tableId])

            if (Compare.areDatasetValuesEqual(self.sourceDatasetSampleData[tableId].SampleData,self.targetDatasetSampleData[tableId].SampleData)):
                rr.Verdict = "Pass"
            else:
                rr.Verdict = "Fail"

            self.sampleDataResults.append(rr)

