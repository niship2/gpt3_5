import streamlit as st
import pandas as pd
import numpy as np
from streamlit_app import check_password
import openai
from gen_sentence import get_completion_title, get_completion_abst, get_completion_claims, get_completion_desc


openai.api_key = st.secrets["OPENAI_API_KEY"]
st.set_page_config(page_title="明細書作成ページ", page_icon="🌍", layout="wide")


# 初期値
try:
    title = st.session_state.title
except:
    title = ""
try:
    abst = st.session_state.abst
except:
    abst = ""
try:
    claims = st.session_state.claims
except:
    claims = ""
try:
    desc = st.session_state.desc
except:
    desc = ""


def get_completion(txt, title="", abst="", claims="", desc="", input_type="title"):
    try:
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
                        "content": "特許文章らしい明細書の文章を作成してください。【発明の詳細な説明】、【技術分野】、【背景技術】、【先行技術文献】、【発明が解決しようとする課題】、【課題を解決するための手段】、【図面の簡単な説明】、【発明を実施するための形態】という見出しをこの順番で加えてください。【背景技術】の部分では先行技術の欠点を説明してください。【先行技術文献】では先行技術文献の番号を入れてください。各見出しで改行して下さい。文章は「である。」「であった。」などの語尾で作成して下さい。"},
                ]
            )
            return response.choices[0].message.content

    except Exception as e:
        return "error!" + st.write(e)


if check_password():
    pd.options.display.precision = 1

    txt = st.text_area(
        'アイデアを入力してください。', '''半導体装置の薄型化と剥離強度の維持をした平板形状の半導体装置を提供する。平板形状のカソード電極の一端に底部が平坦な椀形状部を形成し、前記椀形状部の内部にダイオード素子をはんだ付けし、前記ダイオード素子の上面に、平板形状のアノード電極の一端をはんだ付けし、前記椀形状部の内部を絶縁樹脂で充填した。''')

    st.markdown("---")

    # title###############################################3
    title_inst_col, title_gen_col = st.columns(2)
    with st.container():
        with title_inst_col:
            instruction_title = st.text_area(
                '文章生成指示文を入力してください', value="10文字程度で発明の名称を作成してください。", placeholder="特許文章らしいタイトルを１０文字以内で作成してください。")
        with title_gen_col:
            st.write("発明の名称")
            title = get_completion_title(
                txt, instruction_title=instruction_title)

            st.write(title)

    # abst###############################################3
    st.markdown("---")
    abst_inst_col, abst_gen_col = st.columns(2)

    with st.container():
        with abst_inst_col:
            instruction_abst = st.text_area(
                '文章生成指示文を入力してください', value="特許文章らしい要約を作成してください。【課題】と【解決手段】という見出しを加えてください。であるという語尾で作成して下さい。", placeholder="特許文章らしい要約を作成してください。【課題】と【解決手段】という見出しを加えてください。であるという語尾で作成して下さい。")
        with abst_gen_col:
            st.write("要約")
            abst = get_completion_abst(
                txt, title=title, instruction_title=instruction_title, instruction_abst=instruction_abst)

            st.write(abst)

    # claims###############################################3
    st.markdown("---")
    claims_inst_col, claims_gen_col = st.columns(2)

    with st.container():
        with claims_inst_col:
            instruction_claims = st.text_area(
                '文章生成指示文を入力してください', value="特許文章らしい特許請求の範囲を作成してください。【請求項１】という見出しを加えて下さい。文章はジェプソン形式で１文章で作成して下さい。", placeholder="特許文章らしい特許請求の範囲を作成してください。【請求項１】という見出しを加えて下さい。文章はジェプソン形式で１文章で作成して下さい。")

        with claims_gen_col:
            st.write("請求項")
            if claims == "":
                claims = get_completion_claims(
                    txt, title=title, abst=abst, instruction_title=instruction_title, instruction_abst=instruction_abst, instruction_claims=instruction_claims)
            else:
                claims = st.session_state['claims']
            st.write(claims)

    # desc###############################################3
    st.markdown("---")
    desc_inst_col, desc_gen_col = st.columns(2)

    with st.container():
        with desc_inst_col:
            instruction_desc = st.text_area(
                '文章生成指示文を入力してください', value="特許文章らしい明細書の文章を作成してください。【発明の詳細な説明】、【技術分野】、【背景技術】、【先行技術文献】、【発明が解決しようとする課題】、【課題を解決するための手段】、【図面の簡単な説明】、【発明を実施するための形態】という見出しをこの順番で加えてください。【背景技術】の部分では先行技術の欠点を説明してください。【先行技術文献】では先行技術文献の番号を入れてください。各見出しで改行して下さい。文章は「である。」「であった。」などの語尾で作成して下さい。", placeholder="特許文章らしい明細書の文章を作成してください。【発明の詳細な説明】、【技術分野】、【背景技術】、【先行技術文献】、【発明が解決しようとする課題】、【課題を解決するための手段】、【図面の簡単な説明】、【発明を実施するための形態】という見出しをこの順番で加えてください。【背景技術】の部分では先行技術の欠点を説明してください。【先行技術文献】では先行技術文献の番号を入れてください。各見出しで改行して下さい。文章は「である。」「であった。」などの語尾で作成して下さい。")
        with desc_gen_col:
            st.write("明細書")
            if desc == "":
                desc = get_completion_desc(txt, title=title, abst=abst, instruction_title=instruction_title, instruction_abst=instruction_abst,
                                           instruction_claims=instruction_claims, claims=claims, instruction_desc=instruction_desc)
            else:
                desc = st.session_state['desc']

            st.write(desc)

    # img###############################################3
    st.markdown("---")
    img_inst_col, img_gen_col = st.columns(2)
    with st.container():
        with img_inst_col:
            instruction_img = st.text_area(
                '図面生成指示文を入力してください', value=abst, placeholder="工事中")

            img_response = openai.Image.create(
                prompt=instruction_img,
                n=1,
                size="256x256"
            )
            image_url = img_response['data'][0]['url']
        with img_gen_col:
            st.write("図面")
            st.image(image_url)

    st.session_state['title'] = title
    st.session_state['instruction_title'] = instruction_title
    st.session_state['abst'] = abst
    st.session_state['claims'] = claims
    st.session_state['desc'] = desc

    st.experimental_set_query_params(
        # comp1=comp1,
        # comp2=comp2,
        # ipc_level=ipc_level,
        # appltype=appltype
    )
