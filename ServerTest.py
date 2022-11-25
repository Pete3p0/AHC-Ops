import pymssql
import pandas as pd
import streamlit as st

conn = pymssql.connect(
    host=r"10.10.1.36",
    user=r"ahcsql\ahcadmin",
    password=r"#$#@tlan!s!!@885",
    database='OpsReports'
)
cursor = conn.cursor(as_dict=True)
cursor.execute('SELECT * FROM AdmissionInfo')
data = cursor.fetchall()
data_df = pd.DataFrame(data)

st.dataframe(data_df)

cursor.close()