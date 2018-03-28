
from TestExecution.CreateNewRallyResult import *
from TestExecution.CreateNewTestCases import *
from TestExecution.CreateNewTestCasesResult import *
from TestExecution.RowCountValidation import *
from TestExecution.SampleDataValidation import *
from TestExecution.SchemaValidation import *

if reportType == "TestCase":
    testCase = unittest.TestSuite()
    testCase.addTest(CreateNewTestCases("test_testCaseSetup"))

    unittest.TextTestRunner().run(testCase)

elif reportType == "TestResult":
    testResult = unittest.TestSuite()
    testResult.addTest(CreateNewTestCasesResult("test_rowCountTestResult"))

    unittest.TextTestRunner().run(testResult)

elif reportType == "RallyResult":
    rallyResult = unittest.TestSuite()
    rallyResult.addTest(CreateNewRallyResult("test_rallyResultSetup"))

    unittest.TextTestRunner().run(rallyResult)
	
elif reportType == "FullTestCoverage":
    fullResult = unittest.TestSuite()
    fullResult.addTest(RowCountValidation("test_rowCountValidation"))
    fullResult.addTest(SampleDataValidation("test_sampleDataValidation"))
    fullResult.addTest(SchemaValidation("test_schemaValidation"))

    unittest.TextTestRunner().run(fullResult)



