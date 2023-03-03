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
    instruction_title = st.session_state.instruction_title
    abst = st.session_state.abst
    claims = st.session_state.claims
    desc = st.session_state.desc

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["願書", "要約", "請求項", "明細書", "図面"])

    with tab1:
        st.header("願書")
        st.write(title)

    with tab2:
        st.header("要約")
        st.write(abst)

    with tab3:
        st.header("請求項")
        st.write(claims)
    with tab4:
        st.header("明細書")
        st.write(desc)
    with tab5:
        st.header("図面")
        st.write("庁提出に便利なようにしたい。")
