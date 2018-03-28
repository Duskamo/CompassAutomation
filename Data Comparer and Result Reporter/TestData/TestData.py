
from Models.ColumnSchema import *

class TestData:

    class Source:
        @staticmethod
        def getSampleData():
            dataset = []

            dataset.append([1,"Channing N. Dodson",48,"2016-10-17 14:06:09"])
            dataset.append([2,"Ian K. Austin",30,"2018-03-30 20:01:31"])
            dataset.append([3,"Lee P. Fuentes",28,"2017-09-13 03:22:13"])
            dataset.append([4,"Phelan V. Petty",87,"2016-09-15 07:32:40"])
            dataset.append([5,"Elmo T. Kent",62,"2017-04-07 01:57:35"])
            dataset.append([6,"Dominique F. Hopkins",4,"2017-11-08 15:56:09"])
            dataset.append([7,"Tyler S. Gordon",11,"2017-01-20 05:12:04"])
            dataset.append([8,"Cairo B. Chaney",31,"2017-04-06 00:44:00"])
            dataset.append([9,"Brenda V. Juarez",2,"2018-03-26 07:44:39"])
            dataset.append([10,"Barrett E. Browning",40,"2018-06-01 12:35:47"])

            return dataset

        @staticmethod
        def getSchemaData():
            dataset = [[ColSchema(),ColSchema(),ColSchema(),ColSchema(),ColSchema()],[ColSchema(),ColSchema(),ColSchema()],[ColSchema(),ColSchema()]]

            dataset[0][0].Name = "Col1"
            dataset[0][0].DataType = "varchar"
            dataset[0][1].Name = "Col2"
            dataset[0][1].DataType = "int"
            dataset[0][2].Name = "Col3"
            dataset[0][2].DataType = "float"
            dataset[0][3].Name = "Col4"
            dataset[0][3].DataType = "bit"
            dataset[0][4].Name = "Col5"
            dataset[0][4].DataType = "time"

            dataset[1][0].Name = "Col1"
            dataset[1][0].DataType = "varchar"
            dataset[1][1].Name = "Col2"
            dataset[1][1].DataType = "int"
            dataset[1][2].Name = "Col3"
            dataset[1][2].DataType = "float"

            dataset[2][0].Name = "Col1"
            dataset[2][0].DataType = "varchar"
            dataset[2][1].Name = "Col2"
            dataset[2][1].DataType = "int"

            return dataset

    class Target:
        @staticmethod
        def getSampleData():
            dataset = []

            dataset.append([1,"Channing N. Dodson",48,"2016-10-17 14:06:09"])
            dataset.append([2,"Ian K. Austin",30,"2018-03-30 20:01:31"])
            dataset.append([3,"Lee P. Fuentes",28,"2017-09-13 03:22:13"])
            dataset.append([4,"Phelan V. Petty",87,"2016-09-15 07:32:40"])
            dataset.append([5,"Elmo T. Kent",62,"2017-04-07 01:57:35"])
            dataset.append([6,"Dominique F. Hopkins",4,"2017-11-08 15:56:09"])
            dataset.append([7,"Tyler S. Gordon",11,"2017-01-20 05:12:04"])
            dataset.append([8,"Cairo B. Chaney",31,"2017-04-06 00:44:00"])
            dataset.append([9,"Brenda V. Juarez",2,"2018-03-26 07:44:39"])
            dataset.append([10,"Barrett E. Browning",40,"2018-06-01 12:35:47"])

            return dataset

        @staticmethod
        def getSchemaData():
            dataset = [[ColSchema(),ColSchema(),ColSchema(),ColSchema(),ColSchema()],[ColSchema(),ColSchema(),ColSchema()],[ColSchema(),ColSchema()]]

            dataset[0][0].Name = "Col1"
            dataset[0][0].DataType = "STRING"
            dataset[0][1].Name = "Col2"
            dataset[0][1].DataType = "INTEGER"
            dataset[0][2].Name = "Col3"
            dataset[0][2].DataType = "FLOAT"
            dataset[0][3].Name = "Col4"
            dataset[0][3].DataType = "BOOLEAN"
            dataset[0][4].Name = "Col5"
            dataset[0][4].DataType = "TIME"

            dataset[1][0].Name = "Col1"
            dataset[1][0].DataType = "STRING"
            dataset[1][1].Name = "Col2"
            dataset[1][1].DataType = "INTEGER"
            dataset[1][2].Name = "Col3"
            dataset[1][2].DataType = "FLOAT"

            dataset[2][0].Name = "Col1"
            dataset[2][0].DataType = "STRING"
            dataset[2][1].Name = "Col2"
            dataset[2][1].DataType = "INTEGER"

            return dataset
