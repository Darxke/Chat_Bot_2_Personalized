import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.let_it_rain import rain
from streamlit.components.v1 import html
from streamlit_timeline import st_timeline


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
def my_timeline():
    items = [
        {"id": 1, "content": "Born", "start": "2009-10-27",},
        {"id": 2, "content": "First Brother", "start": "2011-7-20"},
        {"id": 3, "content": "Second Brother", "start": "2018-6-20"},
        {"id": 4, "content": "Started Coding", "start": "2019-8-29"},
        {"id": 5, "content": "Joined Robotics Team", "start": "2021-9-25"},
        {"id": 6, "content": "Moved To Irvine For HS", "start": "2024-8-24"},
        {"id": 7, "content": "Graduate HS", "start": "2028-5-27"},
    ]

    timeline = st_timeline(items, groups=[], options={}, height="300px")
    st.subheader("Selected item")
    st.write(timeline)

