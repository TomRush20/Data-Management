import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

db_path = 'student_alcohol.db'

connection = sqlite3.connect(db_path)

cursor = connection.cursor()

query = """
SELECT sex, AVG(workday_alcohol) AS 'Male_Workday_Consumpton', AVG(weekend_alcohol) AS 'Male_Weekend_Consumption'
FROM student
GROUP BY sex
HAVING sex = 'M';
"""

query_female = """
SELECT sex, AVG(workday_alcohol) AS 'Female_Workday_Consumpton', AVG(weekend_alcohol) AS 'Female_Weekend_Consumption'
FROM student
GROUP BY sex
HAVING sex = 'F';
"""

cursor.execute(query)
results_male = cursor.fetchall()
results_male = pd.DataFrame(results_male)

cursor.execute(query_female)

results_female = cursor.fetchall()
results_female = pd.DataFrame(results_female)

final_df = pd.concat([results_male, results_female], ignore_index=True, axis=0)
final_df.rename(columns={1: 'Workday Alcohol', 2: 'Weekend Alcohol', 0: 'Sex'}, inplace=True)

scatter = px.scatter(final_df, x='Workday Alcohol', y='Weekend Alcohol', color='Sex')
st.plotly_chart(scatter)

connection.close()