import re

class ListReaderWriter:
    def __init__(self,file):
        self.inputFile = file

    def read(self):
        with open(self.inputFile, "r") as f:
            content = f.readlines()

        f.close()

        content = [x.strip() for x in content]

        return content

    def writeListToFile(self,list,outputFile):
        f = open(outputFile,"w")

        for item in list:
            f.write("\"" + item + "\",")

        f.close()

class UchModifier:
    def __init__(self,fullList):
        self.fullList = fullList
        self.initaltables = []
        self.loadedTables = []
        self.uchLatest = []
        self.uchFull = []
        self.uchIncremental = []

    def getTableName(self,table):
        name=""
        for x in table:
            if(x == '_'):
                return name
            name += x

    def filterForInitialLoads(self):
        for i in range(len(self.fullList)):
            table = self.fullList[i]
            previous = self.fullList[i-1]
            name = self.getTableName(table)
            if(i < len(self.fullList)-1):
                next = self.fullList[i+1]
                if(name != self.getTableName(previous)):
                    if(name != self.getTableName(next)):
                        self.uchLatest.append(table)
                    self.initaltables.append(table)
                else:
                    if(name != self.getTableName(next)):
                        self.uchLatest.append(table)
                    else:
                        self.loadedTables.append(table)
            else:
                if(name != self.getTableName(previous)):
                    self.initaltables.append(table)
                else:
                    self.uchLatest.append(table)

    def parseFullAndIncrementalLoads(self):
        for table in self.uchLatest:
            if(bool(re.search('19000101000000000', table))):
                self.uchFull.append(table)
            elif(bool(re.search(r'[0-9]*_[0-9]*_[0-9]*', table))):
                self.uchIncremental.append(table)

    def getLatestLoads(self):
        return self.uchLatest

    def getFullLoads(self):
        return self.uchFull

    def getIncrementalLoads(self):
        return self.uchIncremental



################ start ####################
inputFile = "./input/list_to_load_type/uch_tables_7_6_output.txt"
outputFullFile = "./output/list_to_load_type/uch_tables_7_6_full_tables.txt"
outputIncrementalFile = "./output/list_to_load_type/uch_tables_7_6_incremental_tables.txt"

listReaderWriter = ListReaderWriter(inputFile)
fullList = listReaderWriter.read()

uchModifier = UchModifier(fullList)

uchModifier.filterForInitialLoads()
#uchModifier.filterForLatestLoads()
uchModifier.parseFullAndIncrementalLoads()

uchLatestTables = uchModifier.getLatestLoads()
uchFull = uchModifier.getFullLoads()
uchIncrementals = uchModifier.getIncrementalLoads()

listReaderWriter.writeListToFile(uchFull,outputFullFile)
listReaderWriter.writeListToFile(uchIncrementals,outputIncrementalFile)

