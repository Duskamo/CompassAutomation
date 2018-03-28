from Configuration import *
import xw;t
class Compare:

    @staticmethod
    def areDatasetsCountsEqual(sourceData,targetData):
        return (((int(sourceData) - int(targetData))/int(targetData))*100) <= validationErrorAllowance

    @staticmethod
    def areTableColumnSchemasEqual(sourceTable,targetTable):
        sourceColumnCount = len(sourceTable)
        columnEqualityCount = 0
        isUsed = False

        sourceToTargetMapping = Compare.__getSchemaMapping()

        for column in range(len(sourceTable)):
            for key, values in sourceToTargetMapping.items():
                if sourceTable[column].DataType == key:
                    for value in values:
                        if targetTable[column].DataType == value:
                            columnEqualityCount += 1

        if (sourceColumnCount == columnEqualityCount):
            isUsed = True

        return isUsed

    @staticmethod
    def areDatasetValuesEqual(sourceTable,targetTable):
        sourceValueCount = len(sourceTable) * len(sourceTable[0])
        valueEqualityCount = 0
        isEqual = False

        for rowId in range(len(sourceTable)):
            for colId in range(len(sourceTable[0])):
                if (sourceTable[rowId][colId] == targetTable[rowId][colId]):
                    valueEqualityCount += 1

        if (sourceValueCount == valueEqualityCount):
            isEqual = True

        return isEqual

    @staticmethod
    def __getSchemaMapping():
        return {
            "bigint" : ["INTEGER"],
            "bit" : ["BOOLEAN"],
            "date" : ["DATE"],
            "datetime" : ["DATETIME"],
            "float" : ["FLOAT"],
            "int" : ["INTEGER"],
            "numeric" : ["INTEGER","FLOAT"],
            "nvarchar" : ["STRING"],
            "nchar" : ["STRING"],
            "smallint" : ["INTEGER"],
            "time" : ["TIME","DATETIME"],
            "tinyint" : ["INTEGER"],
            "varchar" : ["STRING"]
        }
