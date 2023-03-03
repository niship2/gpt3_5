import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True


if check_password():
    st.sidebar.write("パスワードはpasswordです")
    st.write("# GPT3.5による特許明細書生成(の夢)")
    st.write("## サイドバーのmakeを押して開始してください。 👋")
    st.markdown(
        "## <font color='red'>注意：[ChatGPTの利用は「公開」にあたるのか？](https://openlegalcommunity.com/chatgpt-public-disclosure/)に記載のとおり、アイデアをサーバに送った時点で、そのアイデアが公開とみなされる可能性がある、とのことなので、もし使う場合利用は試しだけにしてください。</font>")
