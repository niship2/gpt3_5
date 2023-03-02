import streamlit as st
import pandas as pd
import numpy as np
from streamlit_app import check_password
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]


def get_completion(txt, title="", abst="", claims="", desc="", input_type="title"):
    try:
        if input_type == "title":
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                    {"role": "user", "content": "以下の文章に特許文章らしいタイトルを１０文字以内で作成してください。" + txt},
                ]
            )
            return response.choices[0].message.content

        if input_type == "abst":
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                    {"role": "user", "content": "以下の文章に特許文章らしいタイトルを１０文字以内で作成してください。" + txt},
                    {"role": "assistant", "content": title},
                    {"role": "user", "content": "特許文章らしい要約を作成してください。【課題】と【解決手段】という見出しを加えてください。であるという語尾で作成して下さい。"},
                ]
            )
            return response.choices[0].message.content

        if input_type == "claims":
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                    {"role": "user", "content": "以下の文章に特許文章らしいタイトルを１０文字以内で作成してください。" + txt},
                    {"role": "assistant", "content": title},
                    {"role": "user", "content": "特許文章らしい要約を作成してください。【課題】と【解決手段】という見出しを加えてください。であるという語尾で作成して下さい。"},
                    {"role": "assistant", "content": abst},
                    {"role": "user",
                        "content": "特許文章らしい特許請求の範囲を作成してください。【請求項１】という見出しを加えて下さい。文章はジェプソン形式で１文章で作成して下さい。"},
                ]
            )
            return response.choices[0].message.content

        if input_type == "desc":
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは特許文章を作成する人です。"},
                    {"role": "user", "content": "以下の文章に特許文章らしいタイトルを１０文字以内で作成してください。" + txt},
                    {"role": "assistant", "content": title},
                    {"role": "user", "content": "特許文章らしい要約を作成してください。【課題】と【解決手段】という見出しを加えてください。であるという語尾で作成して下さい。"},
                    {"role": "assistant", "content": abst},
                    {"role": "user",
                        "content": "特許文章らしい特許請求の範囲を作成してください。【請求項１】という見出しを加えて下さい。文章はジェプソン形式で１文章で作成して下さい。"},
                    {"role": "assistant", "content": claims},
                    {"role": "user",
                        "content": "特許文章らしい明細書の文章を作成してください。【発明の詳細な説明】、【技術分野】、【背景技術】、【先行技術文献】、【発明が解決しようとする課題】、【課題を解決するための手段】、【図面の簡単な説明】、【発明を実施するための形態】という見出しをこの順番で加えてください。【背景技術】の部分では先行技術の欠点を説明してください。【先行技術文献】では先行技術文献の番号を入れてください。文章は「である。」「であった。」などの語尾で作成して下さい。"},
                ]
            )
            return response.choices[0].message.content

    except Exception as e:
        return "error!" + st.write(e)


if check_password():
    #st.set_page_config(page_title="明細書作成ページ", page_icon="🌍", layout="wide")
    pd.options.display.precision = 1

    txt = st.text_area('アイデアを入力してください。', '''課題】半導体装置の薄型化と剥離強度の維持をした平板形状の半導体装置を提供する。
        【解決手段】平板形状のカソード電極１の一端に底部が平坦な椀形状部１２を形成し、前記椀形状部１２の内部にダイオード素子３をはんだ付けし、前記ダイオード素子３の上面に、平板形状のアノード電極２の一端２１をはんだ付けし、前記椀形状部の内部を絶縁樹脂で充填した。
        ''')

    st.markdown("---")

    title = get_completion(txt, title="", abst="",
                           claims="", desc="", input_type="title")

    with st.expander("発明の名称"):
        st.write(title)

    abst = get_completion(txt, title=title, abst="",
                          claims="", desc="", input_type="abst")

    with st.expander("要約"):
        st.write(abst)

    claims = get_completion(txt, title=title, abst=abst,
                            claims="", desc="", input_type="claims")

    with st.expander("特許請求の範囲"):
        st.write(claims)

    desc = get_completion(txt, title=title, abst=abst,
                          claims=claims, desc="", input_type="desc")

    with st.expander("詳細な説明"):
        st.write(desc)

    with st.expander("図面"):
        st.write("工事中")

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
