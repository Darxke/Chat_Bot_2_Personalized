from streamlit_card import card


hasClicked = card(
  title="Hello World!",
  text="Some description",
  image="./images/apples.png",
  url="https://github.com/gamcoh/st-card"
)
import streamlit as st

on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")