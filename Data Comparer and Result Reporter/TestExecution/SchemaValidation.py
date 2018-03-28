from Utils.TestConditions import *
from SQL.SqlServerManager import *
from SQL.GBQManager import *
from Utils.Compare import *
from Models.RallyResultRC import *



class SchemaValidation(TestConditions):
    def test_schemaValidation(self):
        # Verify source table count matches target table count
        self.assertEqual(len(self.sourceTables),len(self.targetTables))

        # Get table list schema information from source and target databases

        for tableId in range(len(self.sourceTables)):
            sqlServerManager = SqlServerManager(self.SqlServerCursor)
            gbqManager = GBQManager(self.gbqClient)

            sourceTableSchema = sqlServerManager.getSchema(self.sourceTables[tableId])
            targetTableSchema = gbqManager.getSchema(self.targetTables[tableId])

            self.sourceDatasetSchema.append(sourceTableSchema)
            self.targetDatasetSchema.append(targetTableSchema)

        # Compare and validate source and target schema information
        for i in range(len(self.sourceDatasetSchema)):
            rr = RallyResult(self.sourceTables[i], self.targetTables[i])

            if (Compare.areTableColumnSchemasEqual(self.sourceDatasetSchema[i].ColumnSchemaList, self.targetDatasetSchema[i].ColumnSchemaList)):
                rr.Verdict = "Pass"
            else:
                rr.Verdict = "Fail"

            self.schemaResults.append(rr)