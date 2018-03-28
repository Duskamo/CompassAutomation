from google.cloud import bigquery
from google_auth_oauthlib import flow

class GBQConnector:
    def __init__(self,credentials,project,launchBrowser):
        self.Credentials = credentials
        self.Project = project
        self.LaunchBrowser = launchBrowser

        self.Client = None


    def connectToDatabase(self):
        appflow = flow.InstalledAppFlow.from_client_secrets_file(
            self.Credentials,
            scopes=['https://www.googleapis.com/auth/bigquery'])

        if self.LaunchBrowser:
            appflow.run_local_server()
        else:
            appflow.run_console()

        self.Client = bigquery.Client(project=self.Project, credentials=appflow.credentials)

        return self.Client

    def close(self):
        ""