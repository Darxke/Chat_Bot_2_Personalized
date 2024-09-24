#homepage
import streamlit as st
from Css_Testing import add_bg_from_local, bg_sideBar
def home():
    st.markdown("<h1 style='text-align: center; color: black;'>🏠 Homepage</h1>", unsafe_allow_html=True)

def bg_home():
    add_bg_from_local('./images/rocks.jpg')
    bg_sideBar("#d4c3c4")
