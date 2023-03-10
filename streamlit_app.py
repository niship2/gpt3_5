import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="ð",
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
        st.error("ð Password incorrect")
        return False
    else:
        # Password correct.
        return True


st.sidebar.write("ãã¹ã¯ã¼ãã¯passwordã§ã")
if check_password():
    st.write("# GPT3.5ã«ããç¹è¨±æç´°æ¸çæ(ã®å¤¢)")
    st.write("## ãµã¤ããã¼ã®æç« çæãæ¼ãã¦éå§ãã¦ãã ããã ð")
    st.markdown(
        "#### æ³¨æï¼[ChatGPTã®å©ç¨ã¯ãå¬éãã«ãããã®ãï¼](https://openlegalcommunity.com/chatgpt-public-disclosure/)ã«è¨è¼ã®ã¨ãããã¢ã¤ãã¢ããµã¼ãã«éã£ãæç¹ã§ããã®ã¢ã¤ãã¢ãå¬éã¨ã¿ãªãããå¯è½æ§ããããã¨ã®ãã¨ãªã®ã§ãããä½¿ãå ´åå©ç¨ã¯è©¦ãã ãã«ãã¦ãã ããã")
