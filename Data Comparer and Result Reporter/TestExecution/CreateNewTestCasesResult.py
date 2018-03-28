from Utils.TestConditions import *
from Models.TestCaseResult import *
from Utils.Compare import *

class CreateNewTestCasesResult(TestConditions):

    def test_rowCountTestResult(self):
        # validating actual results of if source and target tables are equal in amount
        self.assertEqual(len(self.sourceData),len(self.targetData))

        for i in range(len(self.sourceData)):
            tcr = TestCaseResult(self.sourceData[i].TableName,self.targetData[i].TableName)

            if (Compare.areDatasetsCountsEqual(self.sourceData[i].TableCount,self.targetData[i].TableCount)):
                tcr.Verdict = "Pass"
                tcr.Notes = loadType + " Load:\n"\
                            + "Row counts are equal between " + self.sourceData[i].TableName + " and " + self.targetData[i].TableName + " tables.\n\n"\
                            + self.sourceData[i].TableName + ": " + self.sourceData[i].TableCount + "\n"\
                            + self.targetData[i].TableName + ": " + self.targetData[i].TableCount
            else:
                tcr.Verdict = "Fail"
                tcr.Notes = loadType + " Load:\n"\
                            + "Row counts are not equal between " + self.sourceData[i].TableName + " and " + self.targetData[i].TableName + " tables.\n\n"\
                            + self.sourceData[i].TableName + ": " + self.sourceData[i].TableCount + "\n"\
                            + self.targetData[i].TableName + ": " + self.targetData[i].TableCount

            self.testResults.append(tcr)

