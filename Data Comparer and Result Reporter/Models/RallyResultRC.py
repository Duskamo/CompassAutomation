
from Models.RallyResult import *

class RallyResultRC(RallyResult):
    def __init__(self,sourceTableName,sourceTableCount,targetTableName,targetTableCount):
        super().__init__(sourceTableName,targetTableName)

        self.SourceCount = sourceTableCount
        self.TargetCount = targetTableCount
