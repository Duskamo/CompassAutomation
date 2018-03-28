
from Configuration import *

class TestCase:
    def __init__(self,sourceTableName,targetTableName):
        self.Description = "Rowcount validation of " + sourceTableName + " and " + targetTableName + " table"
        self.Method = "Automated"
        self.Name = "Rowcount validation of CHCO source and GBQ target " + sourceTableName + " table"
        self.PostConditions = ""
        self.PreConditions = "<ol><li>Tester should be logged into GBQ through the VPN, have focus on the hdc-main-dev project, and have a new query window open.</li><li>Current data should be loaded into GBQ CHCO tables in raw_chco dataset.</li></ol>"
        self.Priority = "Important"
        self.Risk = "High"
        self.Type = "Regression"
        self.ValidationExpectedResult = "<ol><li>Query will return a count of all records from the source table. Temporarily document this result.</li><li>Query will return a count of all records from the target table. Temporarily document this result.</li><li>Both results will be equal.</li></ol>"
        self.ValidationInput = "<ol><li>Enter and run Query 1 from the post-condition section of this test case into the GBQ new query window.</li><li>Enter and run Query 2 from the post-condition section of this test case into the GBQ new query window.</li><li>Compare the result obtained from running Query 1 to the result obtained from running Query 2.</li></ol>"
        self.Project = "HDC-GCP"
        self.TestFolder = testFolder
        self.WorkProduct = workProduct