from Utils.TestConditions import *
from Utils.Compare import *
from Models.RallyResultRC import *

class CreateNewRallyResult(TestConditions):

    def test_rallyResultSetup(self):
        # validating actual results of if source and target tables are equal in amount
        self.assertEqual(len(self.sourceData),len(self.targetData))

        for i in range(len(self.sourceData)):
            rr = RallyResultRC(self.sourceData[i].TableName,self.sourceData[i].TableCount,self.targetData[i].TableName,self.targetData[i].TableCount)

            if (Compare.areDatasetsCountsEqual(self.sourceData[i].TableCount,self.targetData[i].TableCount)):
                rr.Verdict = "Pass"
            else:
                rr.Verdict = "Fail"

            self.rallyResults.append(rr)