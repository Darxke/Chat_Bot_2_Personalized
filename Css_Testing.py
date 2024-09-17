import streamlit as st
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
def bg_sideBar():
    # Define your custom CSS
    custom_css = """
    <style>
    [data-testid=stSidebar] {
        background-color: #d4c3c4;
    }
    </style>
    """

    # Apply the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

