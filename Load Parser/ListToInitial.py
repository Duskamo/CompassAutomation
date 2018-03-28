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
        for table in self.fullList:
            if not bool(re.search('_[0-9]*_[0-9]*_[0-9]*', table)):
                self.initaltables.append(table)

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

    def getInitialLoads(self):
        return self.initaltables



################ start ####################
inputFile = "./input/list_to_load_type/uch_tables_6_29_output.txt"
outputInitialFile = "./output/list_to_initial/uch_tables_6_29_initial_tables.txt"

listReaderWriter = ListReaderWriter(inputFile)
fullList = listReaderWriter.read()

uchModifier = UchModifier(fullList)

uchModifier.filterForInitialLoads()

uchInitial = uchModifier.getInitialLoads()

listReaderWriter.writeListToFile(uchInitial,outputInitialFile)

