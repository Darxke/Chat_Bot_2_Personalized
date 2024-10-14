#My Projects
import streamlit as st
from util import cardTab,lottie
def myProjects():
    st.header(":film_projector: My Projects")
    st.subheader("Here are some of my projects and a breif description")
    tab1, tab2 = st.tabs(["Coding Class", "Robotics"])

    with tab1:
        cardTab("Shawn-s-Portfolio github", "https://github.com/Darxke/Shawn-s-Portfolio")
        cardTab("Chat_Bot_2_Personalized ", "https://github.com/Darxke/Chat_Bot_2_Personalized")
    with tab2:
        cardTab("RoadRunner 2023", "https://github.com/Darxke/Roadrunner2023")
        cardTab("FTC_FIRST_DIVE", "https://github.com/Darxke/FTC_FIRST_DIVE")
        cardTab("PowerPlay", "https://github.com/Darxke/PowerPlay")
        with st.sidebar:
            lottie("https://lottie.host/51d76cdb-11ae-4e65-94cc-6ea85d204f39/bxx2mbHD0s.json")


