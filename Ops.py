# Import Libraries
import streamlit as st
import numpy as np
import pandas as pd

def main_page():
    st.markdown("# Main page")
    st.sidebar.markdown("# Main page")
    st.write('This is the first page')

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


