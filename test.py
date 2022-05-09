import os
import glob
import pyodbc
import pandas as pd
from DML import *
from sqlalchemy import create_engine
import urllib
from sqlalchemy.sql import text

song_path = 'C:\Data\SourceData\Songs'
logs_path = 'C:\Data\SourceData\Logs'

df2 = pd.DataFrame()

def dumpData(filePath):
    global df2
    for root, dirs, files in os.walk(filePath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            df = pd.read_json(f, lines=True)
            df2 = df2.append(df)
    

def dumpDataToDB(filePath, table_name):
    global df2
    dumpData(filePath)

    quoted = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=MSI\SQLEXPRESS;DATABASE=master;Trusted_Connection=yes")
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    
    statement = text("drop table if exists " + table_name)
    
    con = engine.connect()
    con.execute(statement)

    df2.to_sql(table_name, schema='dbo', con = engine)
    df2 = pd.DataFrame()

    con.close()

if __name__ == "__main__":
    dumpDataToDB(logs_path, 'dumpLogsData')
    dumpDataToDB(song_path, 'dumpSongData')



