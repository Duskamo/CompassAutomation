
########## File used for Configurating the Automation Testing Framework ##########

# Framework-level configurations
reportType = "FullTestCoverage"  # TestCase | TestResult | RallyResult | FullTestCoverage
outputType = "CSV"  # Excel | CSV
cleanseData = False  # True | False

# New TestCase configurations
testFolder = "row_count_validation"
workProduct = ""

# New TestCaseResult configurations
build = "22.2"

# New RallyResult & TestCaseResult configurations
loadType = "Full"  # Incremental | Full | All
validationErrorAllowance = 0  # values represented as percent (ex. 5 = 5% error allowance)

# input and output file names
TestOutputDirectory = "C:\\Users\\dyano\\Dropbox\\Compass Automation\\Extras\\Test Data"

sourceFile = "./TestData/Input_Files/chco source row count tables.csv"
targetFile = "./TestData/Input_Files/chco target row count tables.csv"

targetUKeyFile = "./TestData/Input_Files/TargetUniqueKeys.csv"
sourceFullFile = "./TestData/Input_Files/SourceTestTables.csv" # "../TestData/Input_Files/uch_tables_6_21_full_tables_source.csv" | "../TestData/Input_Files/SourceTestTables.csv"
sourceIncFile = "./TestData/Input_Files/uch_tables_6_21_incremental_tables_source.csv"
targetFullFile = "./TestData/Input_Files/TargetTestTables.csv" # "../TestData/Input_Files/uch_tables_6_21_full_tables_target.csv" | "../TestData/Input_Files/TargetTestTables.csv"
targetIncFile = "./TestData/Input_Files/uch_tables_6_21_incremental_tables_target.csv"

testCasesOutputFile = "./TestData/Output_Files/TestCases/TestCasesOutput_Build_" + build + ".csv"
testCasesResultsOutputFile = "./TestData/Output_Files/TestCasesResults/TestCasesResultsOutput_Build_" + build + ".csv"
rallyResultsOutputFile = "./TestData/Output_Files/RallyResults/RallyResultsOutput_Build_" + build + ".csv"
rowCountResultsOutputFile = "./TestData/Output_Files/RowCountResults/RowCountOutput_Build_" + build + ".csv"
sampleDataResultsOutputFile = "./TestData/Output_Files/SampleDataResults/SampleDataOutput_Build_" + build + ".csv"
schemaResultsOutputFile = "./TestData/Output_Files/SchemaResults/SchemaOutput_Build_" + build + ".csv"
