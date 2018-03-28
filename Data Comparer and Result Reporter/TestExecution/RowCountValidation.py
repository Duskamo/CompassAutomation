from Utils.TestConditions import *
from Utils.Compare import *
from Models.RallyResultRC import *
from SQL.SqlServerManager import *
from SQL.GBQManager import *

class RowCountValidation(TestConditions):

    def test_rowCountValidation(self):
        # Get Dataset Data

        # validating actual results of if source and target tables are equal in amount
        self.assertEqual(len(self.sourceTables),len(self.targetTables))

        # retrieve source and target table rowcounts from databases
        sqlServerManager = SqlServerManager(self.SqlServerCursor)
        sourceTableNamesAndCounts = sqlServerManager.getFullDatasetTableNameAndRowCount(self.sourceTables)

        gbqManager = GBQManager(self.gbqClient)
        targetTableNamesAndCounts = gbqManager.getFullDatasetTableNameAndRowCount(self.targetTables)

        # Comparing Source and target row counts
        for i in range(len(self.sourceTables)):
            rr = RallyResultRC(sourceTableNamesAndCounts[i].TableName,sourceTableNamesAndCounts[i].TableCount,targetTableNamesAndCounts[i].TableName,targetTableNamesAndCounts[i].TableCount)

            if (Compare.areDatasetsCountsEqual(sourceTableNamesAndCounts[i].TableCount,targetTableNamesAndCounts[i].TableCount)):
                rr.Verdict = "Pass"
            else:
                rr.Verdict = "Fail"

            self.rowCountResults.append(rr)

