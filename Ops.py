# Import Libraries
from calendar import month
from datetime import date
from operator import index
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import datetime

st.set_page_config(layout="wide")

image = Image.open('./AHC Logo.png')
st.image(image,width=300,)

# Columns are 1386 wide

def marketing():
    
    with st.form("# Marketing Report"):
        
        st.markdown("# Marketing Report")
        st.markdown("# Timeframe")
        st.write("Submission to Hospital Manager and Marketing Manager monthly by the 10th")
        Month = st.date_input("End of month: ")
        st.sidebar.markdown("# Marketing Report")
        
    # Admissions
        st.write('1. Admission information - Obtain information from PAM or FM/Accountant')
        
        # Get data
        df_admissions = pd.read_excel("Marketing.xlsx",sheet_name="Admissions")

        # Dataframe - Admissions
        gd_ad = GridOptionsBuilder.from_dataframe(df_admissions)
        gd_ad.configure_default_column(min_column_width=30,editable=False,groupable=True)
        gd_ad.configure_column('Number of admissions',editable=True)
        gridoptions_ad = gd_ad.build()
        grid_response_admissions = AgGrid(df_admissions,gridOptions=gridoptions_ad, update_mode=GridUpdateMode.GRID_CHANGED,theme='balham')

        df_admissions = grid_response_admissions['data']
        df_admissions['Date Submitted'] = Month
        df_admissions['Date Submitted'] = pd.to_datetime(df_admissions['Date Submitted'])

    # GP Visits
        st.write('2. GP Visits - Complete Visits information - time spent in person or telephonic')
        
        # Get data
        df_gp_visits = pd.read_excel("Marketing.xlsx",sheet_name="GP Visits")
        df_gp_visits['Name'] = df_gp_visits['Name'].astype(str)
        df_gp_visits['Date'] = Month
        

        # df_gp_visits['Area'] = df_gp_visits['Area'].astype(str)

        # Dataframe - GP Visits
        # dropdownlist = ('A&E Unit','In patients','Theatre cases')
        gd_gp = GridOptionsBuilder.from_dataframe(df_gp_visits)
        gd_gp.configure_default_column(min_column_width=277,editable=True,groupable=True)

        # gd_gp.configure_column('Area', editable=True,cellEditor='agSelectCellEditor',cellEditorParams={'values':dropdownlist})
        gd_gp.configure_column("Date", editable=True, type=["customDateTimeFormat"], custom_format_string='yyyy-MM-dd')
        df_gp_visits['Date'] = pd.to_datetime(df_gp_visits['Date'])
        
        gridoptions_gp = gd_gp.build()
        grid_response_gp_visits = AgGrid(df_gp_visits,gridOptions=gridoptions_gp, update_mode=GridUpdateMode.GRID_CHANGED,theme='balham')
        df_gp_visits = grid_response_gp_visits['data']

    # Specialist Feedback
        st.write('3. Specialist Feedback - Complete Visits information - time spent in person or telephonic')
                
        # Get data
        df_sf_visits = pd.read_excel("Marketing.xlsx",sheet_name="Specialist Feedback")
        df_sf_visits['Name'] = df_sf_visits['Name'].astype(str)
        df_sf_visits['Date'] = Month

        # Dataframe - Specialist Feedback
        dropdownlist = ('Yes','No','Declined')
        gd_sf = GridOptionsBuilder.from_dataframe(df_sf_visits)
        gd_sf.configure_default_column(min_column_width=231,editable=True,groupable=True)
        gd_sf.configure_column('Facility poster displayed', editable=True,cellEditor='agSelectCellEditor',cellEditorParams={'values':dropdownlist})
        gd_sf.configure_column("Date", editable=True, type=["customDateTimeFormat"], custom_format_string='yyyy-MM-dd')
        df_sf_visits['Date'] = pd.to_datetime(df_sf_visits['Date'])

        gridoptions_sf = gd_sf.build()
        grid_response_sf = AgGrid(df_sf_visits,gridOptions=gridoptions_sf, update_mode=GridUpdateMode.GRID_CHANGED,theme='balham')
        df_sf_visits = grid_response_sf['data']




        submitted = st.form_submit_button('Submit')



    if submitted:
        st.balloons()
        df_admissions
        df_gp_visits
        df_sf_visits
        # st.markdown(grid_response['data'].to_html(), unsafe_allow_html=True)
        # grid_response

    
#     st.write('''1. Admission statistics - Obtain information from PAM or FM/Accountant\n
# 2. GP Visits - Complete Visits information - time spent in person or telephonic
# 3. Specialist Feedback - Complete Visits information - time spent in person or telephonic	
# 4. New Specialist Lead and Feedback - Complete Visits information - time spent in person or telephonic	
# 5. External Company visits - Complete number of vistis to external companies - community	
# 6. Allied Healthcare Provider or CM visits - Complete visits information to Allied provider or external Case Managers	
# 7. Social event or staff wellness events held - Complete all social and wellness events held	
# 8. CPD Event - Complete planned and actual events held	
# 9. Maternity to fill where applicable - Complete marketing packs for facilities that have Maternity	
# 10. Staff orientation fill out estimated cost - New staff orientated in facilities - Macro Induction	
# 11. Media coverage - External medica coverage initiated - adverts/podcasts etc	
# 12. Marketing items, (per item and on hand) - Complete monthly on hand values	
# 13. Travelling - Complete total KM's travelled to estimate travelling costs	
# 14. Marketing budget - Complete butgeted values vs actual spent	
# 15. PSQ Statistics and return rates - Complete to measure PSQ'S returned linked to KPI of 60% return rate	
# 16. PSQ Feedback measurement - Complete to measure overall patient satisfaction with facility and services	
# 17. Top 5 Complaints and action plans - Complete top 5 complaints and action plans to ensure complaints are resolved	
# 18. List your top 10 doctors based on admissions - Complete number of patient admissions per month	
# 19. List your top 10 doctors based on revenue - Complete revenue value for respective month	
# ''')

    


    


def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Marketing Report": marketing,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


