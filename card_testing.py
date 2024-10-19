from streamlit_card import card
import streamlit as st

res = card(
    title="Streamlit Card",
    text="This is a test card",
    image="https://placekitten.com/500/500",
    styles={
        "card": {
            "width": "100px",
            "height": "100px",
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

        },
        "text": {
            "font-family": "serif",
        }
    }
)