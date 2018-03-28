import unittest

from DatabaseConfiguration import *
from SQL.SqlServerConnector import *

class DBConnectionTests(unittest.TestCase):

    def setUp(self):
        ""

    def tearDown(self):
        ""

    def test_SqlServerConnection(self):
        sqlServerConnector = SqlServerConnector(Driver, Server, Database, UID, PWD)

        cursor = sqlServerConnector.connectToDatabase()

        cursor.execute('SELECT * FROM source.dbo.Person')

        for row in cursor:
            print(row)

        self.assertTrue(True)

    def test_GBQConnection(self):
        
        self.assertTrue(True)