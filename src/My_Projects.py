#My Projects
import streamlit as st
def myProjects():
    st.header(":film_projector: My Projects")
    st.subheader("Here are some of my projects and a breif description")
    tab1, tab2 = st.tabs(["Coding Class", "Robotics"])

    with tab1:
            st.link_button("Shawn-s-Portfolio github", "https://github.com/Darxke/Shawn-s-Portfolio")

            st.link_button("Chat_Bot_2_Personalized github", "https://github.com/Darxke/Chat_Bot_2_Personalized")
    with tab2:
        st.link_button("RoadRunner 2023", "https://github.com/Darxke/Roadrunner2023")
        st.link_button("FTC_FIRST_DIVE", "https://github.com/Darxke/FTC_FIRST_DIVE")
        st.link_button("PowerPlay", "https://github.com/Darxke/PowerPlay")
            
