import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

db_path = 'student_alcohol.db'

connection = sqlite3.connect(db_path)

cursor = connection.cursor()

query = """
SELECT
	student.workday_alcohoL,
	grades.final_grade,
	COUNT(final_grade) AS final_grade_count
FROM
	student
INNER JOIN grades
		USING(student_id)
GROUP BY
	student.workday_alcohol,
	grades.final_grade
ORDER BY
	student.workday_alcohol;
"""

cursor.execute(query)
results = cursor.fetchall()
results = pd.DataFrame(results)

add_in = {0: [4, 4, 5, 5], 1: ['A+', 'A', 'A+', 'B'], 2: [0, 0, 0, 0]}
add_in = pd.DataFrame(add_in)

final = pd.concat([results, add_in], axis=0)
st.dataframe(final)

connection.close()