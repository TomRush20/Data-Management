import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

# path to sqlite file
db_path = 'chinook.db'

# connect to the sqlite database
connection = sqlite3.connect(db_path)

# create cursor to execute SQL queries
cursor = connection.cursor()

# Write a SQL query
# Multi-line query is """
query = 'select * from tracks'

# Execute the query
cursor.execute(query)

# Get the results and store
results = cursor.fetchall()

results = pd.DataFrame(results)
print(results)

# close the database connection
connection.close()

st.subheader('SQL Query Results')
st.dataframe(results, use_container_width=True)