import streamlit as st
import numpy as np
import pandas as pd
from streamlit_app import check_password

if check_password():
    pd.options.display.precision = 1

    #st.set_page_config(page_title="Report", page_icon="🌍", layout="wide")

    def file_downloader(filename, file_label='File'):
        with open(filename, 'rb') as f:
            data = f.read()

    #time_stamp = st.session_state.timestamp
    title = st.session_state.title
    abst = st.session_state.abst
    claims = st.session_state.claims
    desc = st.session_state.desc

    st.write(title)
    st.write(abst)
    st.write(claims)
    st.write(desc)
