import openai
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_app import check_password


def get_completion_title(txt, instruction_title):
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


def get_completion_abst(txt, title, instruction_title, instruction_abst, abst):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                {"role": "user", "content": instruction_title + txt},
                {"role": "assistant", "content": title},
                {"role": "user", "content": instruction_abst + abst},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "error!" + st.write(e)


def get_completion_claims(txt, title, abst, instruction_title, instruction_abst, instruction_claims, claims):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                {"role": "user", "content": instruction_title + txt},
                {"role": "assistant", "content": title},
                {"role": "user", "content": instruction_abst},
                {"role": "assistant", "content": abst},
                {"role": "user", "content": instruction_claims + claims}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "error!" + st.write(e)


def get_completion_desc(txt, title, abst, instruction_title, instruction_abst, instruction_claims, claims, instruction_desc):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                {"role": "user", "content": instruction_title + txt},
                {"role": "assistant", "content": title},
                {"role": "user", "content": instruction_abst},
                {"role": "assistant", "content": abst},
                {"role": "user", "content": instruction_claims},
                {"role": "assistant", "content": claims},
                {"role": "user", "content": instruction_desc},

            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "error!" + st.write(e)
