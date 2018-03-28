
# File used for configuring connection variables for Compass SQL Server and GBQ Databases

# Sql Server Configuration
Driver = "{SQL Server Native Client 11.0}"
Server = "LAPTOP-VM3M77PB\SQLEXPRESS" # "LAPTOP-VM3M77PB\SQLEXPRESS;" | "DDCL-LANDRY\SQLEXPRESS"
Database = "Source"
UID = "LAPTOP-VM3M77PB\dyano" # "LAPTOP-VM3M77PB\dyano" | "PERFICIENT\dustin.landry"
PWD = ""

# GBQ Configuration
Project = "datademo-156016" # "hdc-main-dev" | "datademo-156016"
Dataset = "Target" # "raw_uchealth" | "Target"
GBQCredentials = "./Auth/client-secrets.json"
LaunchBrowser = True