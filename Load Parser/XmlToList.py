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

    def convertXMLFileToList(self):
        tree = ET.parse(self.fileName)

        root = tree.getroot()
        self.list = root.findall("./tr/td[2]")

        self.file.close()

    def outputListToFile(self,file):
        f = open(file,'w+')

        for i in self.list:
            f.write(i.text.strip() + "\n")

        f.close()

################ start ####################
inputFile = "./input/xml_to_list/uch_tables_7_6.xml"
outputFile = "./output/xml_to_list/uch_tables_7_6_output.txt"

converter = XmlToList()

converter.setInputFile(inputFile)
converter.convertXMLFileToList()
converter.outputListToFile(outputFile)