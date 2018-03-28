import argparse
import time
import uuid

from DatabaseConfiguration import *
from google.cloud import bigquery
from google_auth_oauthlib import flow


def wait_for_job(job):
    while True:
        job.reload()  # Refreshes the state via a GET request.
        if job.state == 'DONE':
            if job.error_result:
                raise RuntimeError(job.errors)
            return
        time.sleep(1)


def run_query(credentials, project, query):
    client = bigquery.Client(project=project, credentials=credentials)
    query_job = client.run_async_query(str(uuid.uuid4()), query)
    query_job.use_legacy_sql = False
    query_job.begin()

    wait_for_job(query_job)

    # Drain the query results by requesting a page at a time.
    query_results = query_job.results()
    page_token = None

    while True:
        rows, total_rows, page_token = query_results.fetch_data(
            max_results=10,
            page_token=page_token)

        for row in rows:
            print(row)

        if not page_token:
            break


def authenticate_and_query(project, query, launch_browser=True):
    appflow = flow.InstalledAppFlow.from_client_secrets_file(
        '../Auth/client-secrets.json',
        scopes=['https://www.googleapis.com/auth/bigquery'])

    if launch_browser:
        appflow.run_local_server()
    else:
        appflow.run_console()

        run_query(appflow.credentials, project, query)


if __name__ == '__main__':
    project = "datademo-156016"
    query1 = "SELECT * FROM `datademo-156016.Target.Person_UCH_CDW_20170620111203696_19000101000000000_20170620111203696` LIMIT 1000"
    launch_browser = False

    authenticate_and_query(Project, query1, launch_browser=launch_browser)