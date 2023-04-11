import streamlit as st
import pandas as pd
import numpy as np
from streamlit_app import check_password
import openai
from gen_sentence import (
    get_completion_title,
    get_completion_abst,
    get_completion_claims,
    get_completion_desc,
)

openai.api_key = st.secrets["API-KEY"]
openai.api_type = "azure"
openai.api_base = st.secrets["OPENAI_API_BASE"]
openai.api_version = "2023-03-15-preview"


st.set_page_config(page_title="明細書作成ページ", page_icon="🌍", layout="wide")

option = st.sidebar.selectbox("生成モデル選択", ("gpt-3.5", "gpt-4"))

# 初期値
try:
    txt = st.session_state.txt
except:
    txt = "半導体装置の薄型化と剥離強度の維持をした平板形状の半導体装置を提供する。平板形状のカソード電極の一端に底部が平坦な椀形状部を形成し、前記椀形状部の内部にダイオード素子をはんだ付けし、前記ダイオード素子の上面に、平板形状のアノード電極の一端をはんだ付けし、前記椀形状部の内部を絶縁樹脂で充填した。"
    st.session_state["txt"] = txt

try:
    title = st.session_state.title
except:
    title = ""
    st.session_state["title"] = title
try:
    abst = st.session_state.abst
except:
    abst = ""
    st.session_state["abst"] = abst
try:
    claims = st.session_state.claims
except:
    claims = ""
    st.session_state["claims"] = claims

try:
    instruction_claims_text = st.session_state.instruction_claims_text
except:
    instruction_claims_text = ""
    st.session_state["instruction_claims_text"] = instruction_claims_text

try:
    desc = st.session_state.desc
except:
    desc = ""
    st.session_state["desc"] = desc

try:
    instruction_desc_text = st.session_state.instruction_desc_text
except:
    instruction_desc_text = ""
    st.session_state["instruction_desc_text"] = instruction_desc_text


def merge_instruction(opts, tex):
    # 初期値で空要素が入ってしまうので削除
    tex_list = []
    tex_list = [x for x in tex.replace("\n", "").split("。") if x != ""]
    for opt in opts:
        if opt in tex_list:
            pass
        else:
            tex_list.append(opt)
    return tex_list


if check_password():
    pd.options.display.precision = 1

    txt = st.text_area("アイデアを入力してください。", txt)

    st.markdown("---")

    # title###############################################3
    title_inst_col, title_gen_col = st.columns(2)
    with st.container():
        with title_inst_col:
            instruction_title = st.text_area(
                "文章生成指示文を入力してください",
                value="10文字程度で発明の名称を作成してください。",
                placeholder="特許文章らしいタイトルを１０文字以内で作成してください。",
            )
            if st.button("名称作成！"):
                title = get_completion_title(txt, instruction_title=instruction_title)
                st.info("アイデア部分の文章と文章生成指示文をもとに作成しました。")
            else:
                title = st.session_state["title"]
        with title_gen_col:
            st.text_area("発明の名称", value=title)

    # abst###############################################3
    st.markdown("---")
    abst_inst_col, abst_gen_col = st.columns(2)

    with st.container():
        with abst_inst_col:
            instruction_abst = st.text_area(
                "要約生成指示文を入力してください",
                value="特許文章らしい要約として修正してください。【課題】と【解決手段】という見出しを加えてください。であるという語尾で作成して下さい。",
                placeholder="特許文章らしい要約を作成してください。【課題】と【解決手段】という見出しを加えてください。であるという語尾で作成して下さい。",
            )
            if st.button("要約修正！"):
                abst = get_completion_abst(
                    txt,
                    title=title,
                    instruction_title=instruction_title,
                    instruction_abst=instruction_abst,
                    abst=abst,
                )
                st.info("アイデア、タイトル、要約生成指示文をもとに作成しました。")
            else:
                abst = st.session_state["abst"]
        with abst_gen_col:
            st.text_area("要約", value=abst, height=200)

    # claims###############################################3
    st.markdown("---")
    claims_inst_col, claims_gen_col = st.columns(2)

    with st.container():
        with claims_inst_col:
            instruction_claim_opt = st.multiselect(
                "指示文例選択",
                default=["特許文章らしい特許請求の範囲で記載してください"],
                options=(
                    "特許文章らしい特許請求の範囲で記載してください",
                    "各特許請求の範囲は１文で作成して下さい",
                    "【請求項１】という見出しを加えて下さい",
                    "【請求項2】を追加して、請求項2には請求項１の構成のどれかを具体化したものとして生成してください",
                ),
            )
            instruction_claims_text = (
                "。\n".join(
                    merge_instruction(instruction_claim_opt, instruction_claims_text)
                )
                + "。"
            )  # 最後の分に。を付加
            instruction_claims = st.text_area(
                "請求項生成指示文を直接入力or選択で作成してください",
                value=instruction_claims_text,
                placeholder="",
                height=250,
            )

            if st.button("請求項修正！"):
                claims = get_completion_claims(
                    txt,
                    title=title,
                    abst=abst,
                    instruction_title=instruction_title,
                    instruction_abst=instruction_abst,
                    instruction_claims=instruction_claims,
                    claims=claims,
                )
                st.info("アイデア、タイトル、要約、請求項生成指示文をもとに作成しました。")

            else:
                claims = st.session_state["claims"]

        with claims_gen_col:
            st.text_area("請求項", value=claims, height=400)

    # desc###############################################3
    st.markdown("---")
    desc_inst_col, desc_gen_col = st.columns(2)

    with st.container():
        with desc_inst_col:
            instruction_desc_opt = st.multiselect(
                "指示文例選択",
                default=["特許文章らしい明細書の文章として修正してください"],
                options=(
                    "特許文章らしい明細書の文章として修正してください",
                    "文章毎に【0001】のように見出しを追加してください",
                    "各見出しで改行して下さい",
                    "文章は「である」「であった」などの語尾で作成して下さい"
                    "【発明の詳細な説明】、【技術分野】、【背景技術】、【先行技術文献】、【発明が解決しようとする課題】、【課題を解決するための手段】、【図面の簡単な説明】、【発明を実施するための形態】という見出しをこの順番で加えてください",
                    "【背景技術】の部分では先行技術の欠点を説明してください",
                    "【先行技術文献】では先行技術文献の番号を入れてください",
                    "【課題を解決するための手段】には生成した特許請求の範囲の文章を記載してください。"
                    "【発明の詳細な説明】は５段落作成して請求項の各構成部品について具体例を記載してください。",
                ),
            )
            instruction_desc_text = (
                "。\n".join(
                    merge_instruction(instruction_desc_opt, instruction_desc_text)
                )
                + "。"
            )  # 最後の分に。を付加
            instruction_desc = st.text_area(
                "明細書生成指示文を直接入力or選択で入力してください",
                value=instruction_desc_text,
                placeholder="",
                height=250,
            )
            if st.button("明細書修正！"):
                desc = get_completion_desc(
                    txt,
                    title=title,
                    abst=abst,
                    instruction_title=instruction_title,
                    instruction_abst=instruction_abst,
                    instruction_claims=instruction_claims,
                    claims=claims,
                    instruction_desc=instruction_desc,
                )
                st.info("アイデア、タイトル、要約、請求項、明細書生成指示文をもとに作成しました。")
            else:
                desc = st.session_state["desc"]
        with desc_gen_col:
            st.text_area("明細書", value=desc, height=400)

    # img###############################################3
    st.markdown("---")
    img_inst_col, img_gen_col = st.columns(2)
    with st.container():
        with img_inst_col:
            instruction_img = st.text_area(
                "図面生成指示文を入力してください", value=title, placeholder="工事中"
            )

            if st.button("図面生成"):
                pass
                # img_response = openai.Image.create(
                #    prompt=instruction_img,
                #    n=1,
                #    size="256x256"
                # )
                # image_url = img_response['data'][0]['url']
        with img_gen_col:
            pass
            # st.write("図面")
            # try:
            #    st.image(image_url)
            # except:
            #    pass

    st.session_state["txt"] = txt
    st.session_state["title"] = title
    st.session_state["instruction_title"] = instruction_title
    st.session_state["abst"] = abst
    st.session_state["claims"] = claims
    st.session_state["desc"] = desc
    st.session_state["option"] = option
    st.session_state["instruction_claims_text"] = instruction_claims_text
    st.session_state["instruction_desc_text"] = instruction_desc_text

    st.experimental_set_query_params(
        # comp1=comp1,
        # comp2=comp2,
        # ipc_level=ipc_level,
        # appltype=appltype
    )
