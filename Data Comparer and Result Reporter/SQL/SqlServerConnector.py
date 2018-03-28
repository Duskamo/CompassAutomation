import pyodbc

class SqlServerConnector:
    def __init__(self,driver,server,database,username,password):
        self.driver = driver
        self.server = server
        self.database = database
        self.uid = username
        self.pwd = password

        self.connection = ""
        self.cursor = ""


    def connectToDatabase(self):
        self.connection = pyodbc.connect("Driver=" + self.driver + ';' +
                                         "Server=" + self.server + ';' +
                                         "Database=" + self.database + ';' +
                                         'Trusted_Connection=yes;'
                                         )

        return self.connection.cursor()

    def close(self):
        self.connection.close()