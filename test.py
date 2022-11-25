# Import libraries

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

# Functions

@st.cache
def data_upload():
    df = pd.read_excel("Marketing.xlsx",sheet_name="Admissions")
    return df

df = data_upload()
# st.dataframe(df)


gd = GridOptionsBuilder.from_dataframe(df)
# gd.configure_pagination(enabled=True)
gd.configure_default_column(min_column_width=351,editable=False,groupable=True)
gd.configure_column('Number of admissions',editable=True)

# sel_mode = st.radio('Selection Type', options=['single', 'multiple'])
# gd.configure_selection(selection_mode=sel_mode,use_checkbox=True)
gridoptions = gd.build()
AgGrid(df,gridOptions=gridoptions)