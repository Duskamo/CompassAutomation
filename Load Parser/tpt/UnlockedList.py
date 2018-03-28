import xml.etree.ElementTree as ET

class XmlToList:
    def __init__(self):
        self.file = None
        self.fileName = None
        self.fileContents = None
        self.list = []

    def setInputFile(self,file):
        self.fileName = file
        self.file = open(file,'r')
        self.fileContents = self.file.read()

    def convertXMLFileToUnlockedList(self):
        tree = ET.parse(self.fileName)

        root = tree.getroot()
        self.list = root.findall("./tr")

        self.file.close()

        for i in self.list:
            if i.find("./td[2]/a[@class='ui-commandlink ']") is not None:
                print(i.find("./td[1]").text)

    def outputListToFile(self,file):
        f = open(file,'w+')

        for i in self.list:
            f.write(i.text + "\n")

        f.close()

inputFile = "./input/skills_list2.xml"
outputFile = "./output/unlockedlist_output.txt"

converter = XmlToList()

converter.setInputFile(inputFile)
converter.convertXMLFileToUnlockedList()
#converter.outputListToFile(outputFile)