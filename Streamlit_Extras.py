import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.let_it_rain import rain
from streamlit.components.v1 import html

def coffee():
    with st.sidebar:
        button(username="shixuanzhuk", floating=False, width=221)


def rainEmojis(emoji):
    rain(
        emoji=emoji,
        font_size=50,
        falling_speed=1,
        animation_length="short",
    )

