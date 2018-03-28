
import csv
from Models.SQLTestResult import *
from Models.TestCase import *

class DataIO:
    @staticmethod
    def readData(file):
        reader = csv.reader(open(file, "rt"))
        data = []

        for row in reader:
            data.append(row[0])

        return data

    @staticmethod
    def readRowCountData(file):
        reader = csv.reader(open(file,"rt"))
        data = []

        for row in reader:
            data.append(SQLTestResult(row[0],row[1]))

        return data

    @staticmethod
    def writeDataForTestCases(file,testCases):
        with open(file, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Description', 'Project', 'TestFolder', 'WorkProduct', 'Type', 'Priority', 'Method', 'Risk', 'PreConditions', 'PostConditions', 'ValidationInput', 'ValidationExpectedResult']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for i in range(len(testCases)):
                writer.writerow({'Name': testCases[i].Name, 'Description': testCases[i].Description, 'Project': testCases[i].Project, 'TestFolder': testCases[i].TestFolder, 'WorkProduct': testCases[i].WorkProduct, 'Type': testCases[i].Type, 'Priority': testCases[i].Priority, 'Method': testCases[i].Method, 'Risk': testCases[i].Risk, 'PreConditions': testCases[i].PreConditions, 'PostConditions': testCases[i].PostConditions, 'ValidationInput': testCases[i].ValidationInput, 'ValidationExpectedResult': testCases[i].ValidationExpectedResult})

            csvfile.close()

    @staticmethod
    def writeDataForTestResults(file,testResults):
        with open(file, 'w', newline='') as csvfile:
            fieldnames = ['Build', 'Date', 'Notes', 'TestCase', 'Verdict']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for i in range(len(testResults)):
                writer.writerow({'Build': testResults[i].Build, 'Date': testResults[i].Date, 'Notes': testResults[i].Notes, 'TestCase': testResults[i].TestCase, 'Verdict': testResults[i].Verdict})

            csvfile.close()

    @staticmethod
    def writeDataForRowCountRallyResults(file,rallyResults):
        with open(file, 'w', newline='') as csvfile:
            fieldnames = ['Test Date', 'Load Type', 'Source Table Name', 'Target Table Name', 'Source Count', 'Target Count', 'Verdict']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for i in range(len(rallyResults)):
                writer.writerow({'Test Date': rallyResults[i].TestDate, 'Load Type': rallyResults[i].LoadType, 'Source Table Name': rallyResults[i].SourceTableName, 'Target Table Name': rallyResults[i].TargetTableName, 'Source Count': rallyResults[i].SourceCount, 'Target Count': rallyResults[i].TargetCount, 'Verdict': rallyResults[i].Verdict})

            csvfile.close()


    @staticmethod
    def writeDataForRallyResults(file,rallyResults):
        with open(file, 'w', newline='') as csvfile:
            fieldnames = ['Test Date', 'Load Type', 'Source Table Name', 'Target Table Name', 'Verdict']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for i in range(len(rallyResults)):
                writer.writerow({'Test Date': rallyResults[i].TestDate, 'Load Type': rallyResults[i].LoadType, 'Source Table Name': rallyResults[i].SourceTableName, 'Target Table Name': rallyResults[i].TargetTableName, 'Verdict': rallyResults[i].Verdict})

            csvfile.close()


    @staticmethod
    def readIDData(file):
        reader = csv.reader(open(file,"rt"))
        data = {}
        for row in reader:
            data[row[0]] = row[1] 
        return data
