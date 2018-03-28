from Configuration import *
from datetime import date

class RallyResult:
    def __init__(self,sourceTableName,targetTableName):
        self.TestDate = str(date.today())
        self.SourceTableName = sourceTableName
        self.TargetTableName = targetTableName
        self.Verdict = ""
        self.LoadType = loadType