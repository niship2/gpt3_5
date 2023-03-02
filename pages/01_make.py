import streamlit as st
import pandas as pd
import numpy as np
from streamlit_app import check_password
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]


def get_compilation(txt, title="", abst="", claims="", desc="", input_type="title"):
    if input_type == "title":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                {"role": "user", "content": "以下の文章に特許文章らしいタイトルを付けてください。" + txt},
            ]
        )

    return response.choices[0].message.content


if check_password():
    #st.set_page_config(page_title="明細書作成ページ", page_icon="🌍", layout="wide")
    pd.options.display.precision = 1

    txt = st.text_area('Text to analyze', '''
        【課題】半導体装置の薄型化と剥離強度の維持をした平板形状の半導体装置を提供する。
        【解決手段】平板形状のカソード電極１の一端に底部が平坦な椀形状部１２を形成し、前記椀形状部１２の内部にダイオード素子３をはんだ付けし、前記ダイオード素子３の上面
            に、平板形状のアノード電極２の一端２１をはんだ付けし、前記椀形状部の内部を絶縁樹脂で充填した。
        ''')

    title = get_compilation(txt, title="", abst="",
                            claims="", desc="", input_type="title")
    st.write(title)

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
