from Configuration import *
from datetime import date

class TestCaseResult:
    def __init__(self,sourceTableName,targetTableName):
        self.Build = build
        self.Date = str(date.today())
        self.Notes = ""
        self.TestCase = "Rowcount validation of CHCO source and GBQ target " + sourceTableName + " table"
        self.Verdict = ""