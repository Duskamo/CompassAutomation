
class DataHandler:

    @staticmethod
    def cleanSourceData(sourceData,targetData):

        newSourceData = []

        for i in range(len(sourceData)):
            for j in range(len(targetData)):
                if DataHandler.__targetTableHasSourceTable(sourceData,i,targetData,j):
                    newSourceData.append(sourceData[i])

        return newSourceData

    @staticmethod
    def ListToCommaString(list):
        uidsString = ""

        for uid in list:
            uidsString += str(uid) + ','

        return uidsString[:-1]

    @staticmethod
    def ListToQuotedCommaString(list):
        tableString = ""

        for item in list:
            tableString += '"' + str(item) + '",'

        return tableString[:-1]

    @staticmethod
    def getUIDsFromTargetTable(targetTable):
        list = []

        for targetRow in range(len(targetTable.SampleData)):
            list.append(targetTable.SampleData[targetRow][0])

        return list

    # private methods
    @staticmethod
    def __targetTableHasSourceTable(sourceData,i,targetData,j):
        return sourceData[i].TableName == targetData[j].TableName[0:targetData[j].TableName.index('_')]
