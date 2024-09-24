import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.let_it_rain import rain
def coffee():
    button = """
    <script type="text/javascript" src="https://buymeacoffee.com/shixuanzhuk" data-name="bmc-button" data-slug="adof6qkj3h" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
    """
def rainEmojis(emoji):
    rain(
        emoji=emoji,
        font_size=50,
        falling_speed=1,
        animation_length="short",
    )

