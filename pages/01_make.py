import streamlit as st
import pandas as pd
import numpy as np
from streamlit_app import check_password

if check_password():
    st.set_page_config(page_title="明細書作成ページ", page_icon="🌍", layout="wide")

    def file_downloader(filename, file_label='File'):
        with open(filename, 'rb') as f:
            data = f.read()

    pd.options.display.precision = 1

    tite = ""
    abst = ""
    claims = ""
    desc = ""

    st.session_state['title'] = title
    st.session_state['abst'] = abst
    st.session_state['claims'] = claims
    st.session_state['desc'] = desc

    st.experimental_set_query_params(
        # comp1=comp1,
        # comp2=comp2,
        # ipc_level=ipc_level,
        # appltype=appltype
    )
