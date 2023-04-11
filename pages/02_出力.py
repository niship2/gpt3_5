import streamlit as st
import numpy as np
import pandas as pd
from streamlit_app import check_password
import time

if check_password():
    pd.options.display.precision = 1

    with st.sidebar.container():
        if st.sidebar.button("提出！", use_container_width=True):
            placeholder = st.empty()
            with placeholder.container():
                time.sleep(2)
                st.info("提出できませんでした", icon="ℹ️")
            time.sleep(3)
            placeholder.empty()

    # st.set_page_config(page_title="Report", page_icon="🌍", layout="wide")

    def file_downloader(filename, file_label="File"):
        with open(filename, "rb") as f:
            data = f.read()

    # time_stamp = st.session_state.timestamp
    title = st.session_state.title
    instruction_title = st.session_state.instruction_title
    abst = st.session_state.abst
    claims = st.session_state.claims
    desc = st.session_state.desc

    try:
        bibtable = st.session_state.bibtable
    except:
        bibtable = pd.DataFrame()
        st.session_state["bibtable"] = bibtable

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["願書", "要約", "請求項", "明細書", "図面"])

    with tab1:
        df = pd.DataFrame(
            [
                {"項目": "願書", "値": ""},
                {"項目": "【書類名】", "値": "特許願"},
                {"項目": "【整理番号】", "値": "***"},
                {"項目": "【提出日】", "値": "令和 年 月 日"},
                {"項目": "【あて先】", "値": "特許庁長官 殿"},
                {"項目": "【国際特許分類】", "値": "***"},
                {"項目": "【発明者】", "値": "***"},
                {"項目": "【住所又は居所】", "値": "***"},
                {"項目": "【氏名】", "値": "***"},
                {"項目": "【特許出願人】", "値": "***"},
                {"項目": "【識別番号】", "値": "***"},
                {"項目": "【住所又は居所】", "値": "***"},
                {"項目": "【氏名又は名称】", "値": "***"},
                {"項目": "【提出物件の目録】", "値": ""},
                {"項目": "【物件名】 特許請求の範囲", "値": "1"},
                {"項目": "【物件名】 明細書", "値": "1"},
                {"項目": "【物件名】 図面", "値": "1"},
                {"項目": "【物件名】 要約書", "値": "1"},
            ]
        )
        with st.expander("願書編集"):
            st.write("セルをクリックして編集できます。")
            st.write("エクセル等からコピペできます。")
            bibtable = st.experimental_data_editor(df, width=400, num_rows="dynamic")

        for index, row in bibtable.iterrows():
            st.write(row["項目"] + str(row["値"]))

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

        for i in range(0, len(desc_temp_list) - 1):
            desc_out += desc_temp_list[i]
        st.write(desc_out)
    with tab5:
        st.header("図面")
        st.write("庁提出に便利なようにしたい。")
