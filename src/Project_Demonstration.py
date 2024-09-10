#Project Demonstration
import streamlit as st
from src_2.landing_1 import introduction
from src_2.setup_2 import setup
from src_2.basic_3 import basicStreamlitElements
from src_2.interative_4 import interativeApp
from src_2.run_5 import runApp
from src_2.capturing_6 import capturingVariables
from src_2.hands_7 import handsOnActivity
from src_2.wrap_8 import wrapUp
from src_2.todo_9 import toDoList
from src_2.quiz_10 import quiz
def project_Demonstration():
    st.header("Demonstrations")
    st.subheader("Time for some demonstration!")
    tab1, tab2, tab3 = st.tabs(["Shawn's Portfolio", "Chat_Bot_2_Personalized", "RoadRunner 2023"])
    with tab1:
        st.title("Intro to streamlit :dark_sunglasses:")


        #add a sidebar
        st.sidebar.title("Lesson section")
        sections = [
            ":one: Introduction",
            ":two: Setup",
            ":three: Basic Streamlit Elements",
            ":four: Simple Interative App",
            ":five: Running the App",
            ":six: Capturing Variables",
            ":seven: Hands on Activity",
            ":eight: :red[Wrap up]" ,
            ":nine: ToDo List",
            ":one::zero: Quiz",
            

        ]

        selected_section = st.sidebar.radio("Go to", sections)
        #main content
        if selected_section == ":one: Introduction":
            introduction()
        elif selected_section == ":two: Setup":
            setup()
        elif selected_section == ":three: Basic Streamlit Elements":
            basicStreamlitElements()
        elif selected_section == ":four: Simple Interative App":
            interativeApp()
        elif selected_section == ":five: Running the App":
            runApp()
        elif selected_section == ":six: Capturing Variables":
            capturingVariables()
        elif selected_section == ":seven: Hands on Activity":
            handsOnActivity()
        elif selected_section == ":eight: :red[Wrap up]":
            wrapUp()
        elif selected_section == ":nine: ToDo List":
            toDoList()
        elif selected_section == ":one::zero: Quiz":
            quiz()
    with tab2:
        st.write("The project you are currently using is Chat_Bot_2_Personalized.")
    with tab3:
        st.write("Roadrunner is a library used in FTC for precision. ")
        
