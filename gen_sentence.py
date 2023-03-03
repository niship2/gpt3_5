import openai
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_app import check_password


def get_completion_title(txt, instruction_title="以下の文章に特許文章らしいタイトルを１０文字以内で作成してください。"):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                {"role": "user", "content": instruction_title + txt},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "error!" + st.write(e)


def get_completion_abst(txt, title, instruction_title, instruction_abst="特許文章らしい要約を作成してください。【課題】と【解決手段】という見出しを加えてください。であるという語尾で作成して下さい。"):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                {"role": "user", "content": instruction_title + txt},
                {"role": "assistant", "content": title},
                {"role": "user", "content": instruction_abst},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "error!" + st.write(e)
