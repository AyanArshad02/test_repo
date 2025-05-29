import sqlite3
import pandas as pd

df=pd.read_csv("data.csv")

connection=sqlite3.connect("test_ticket.db")

df.to_sql("ticket",connection,if_exists="replace")

connection.close()