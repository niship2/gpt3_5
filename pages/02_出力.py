import streamlit as st
import numpy as np
import pandas as pd
from streamlit_app import check_password

if check_password():
    pd.options.display.precision = 1

    # st.set_page_config(page_title="Report", page_icon="🌍", layout="wide")

    def file_downloader(filename, file_label='File'):
        with open(filename, 'rb') as f:
            data = f.read()

    # time_stamp = st.session_state.timestamp
    title = st.session_state.title
    instruction_title = st.session_state.instruction_title
    abst = st.session_state.abst
    claims = st.session_state.claims
    desc = st.session_state.desc

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["願書", "要約", "請求項", "明細書", "図面"])

    with tab1:
        st.header("願書")
        st.write("【書類名】 特許願")
        st.write("【整理番号】")
        st.write("【提出日】 令和 年 月 日")
        st.write("【あて先】 特許庁長官 殿")
        st.write("【国際特許分類】")
        st.write("【発明者】")
        st.write("【住所又は居所】")
        st.write("【氏名】")
        st.write("【特許出願人】")
        st.write("【識別番号】）")
        st.write("【住所又は居所】")
        st.write("【氏名又は名称】")
        st.write("（【代表者】）")
        st.write("（【国籍・地域】）")
        st.write("（【電話番号】）")
        st.write("【提出物件の目録】")
        st.write("【物件名】 特許請求の範囲 １")
        st.write("【物件名】 明細書 １")
        st.write("（【物件名】 図面 １）")
        st.write("【物件名】 要約書 １")

    with tab2:
        st.header("要約")
        st.write("【書類名】 要約書")
        st.write("【要約】")
        st.write(abst)
        st.write("【選択図】　図１")

    with tab3:
        st.header("請求項")
        st.write("【書類名】 特許請求の範囲")
        st.write(claims)
    with tab4:
        st.header("明細書")
        st.write("【書類名】 明細書")
        st.write("【発明の名称】" + title)

        desc_temp_list = desc.split("。")

        desc_out = ""

        for i in range(0, len(desc_temp_list)-1):
            desc_out += "【" + str(i+1).zfill(4) + "】" + \
                desc_temp_list[i] + "。\r\n"
        st.write(desc_out)
    with tab5:
        st.header("図面")
        st.write("庁提出に便利なようにしたい。")
