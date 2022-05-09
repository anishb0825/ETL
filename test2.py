from sqlalchemy import create_engine
import urllib
import pyodbc
import pandas as pd
import os
import glob
import json

df2 = pd.DataFrame()
logs_path = 'C:\Data\SourceData\Logs'

for root, dirs, files in os.walk(logs_path):
    files = glob.glob(os.path.join(root,'*.json'))
    for f in files :
        df = pd.read_json(f, lines=True)
        df2 = df2.append(df)


quoted = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=MSI\SQLEXPRESS;DATABASE=master;Trusted_Connection=yes")
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

df2.to_sql('dump_logsdata', schema='dbo', con = engine)