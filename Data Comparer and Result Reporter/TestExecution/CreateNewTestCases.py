from Utils.TestConditions import *

class CreateNewTestCases(TestConditions):

    def test_testCaseSetup(self):
        # validating actual results of if source and target tables are equal in amount
        self.assertEqual(len(self.sourceData),len(self.targetData))

        for i in range(len(self.sourceData)):
            self.testCases.append(TestCase(self.sourceData[i].TableName,self.targetData[i].TableName))
