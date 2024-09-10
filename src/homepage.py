#homepage
import streamlit as st
def home(): 
    st.header(":one: Introduction")
    st.subheader(":one: Lesson plan for beginner coders")
    st.write("Streamlit is a Python libary that makes it easy to create web apps.")
    if st.button("Show Example App"):
        st.code('''
import streamlit as st
st.title("Hello, Streamlit!")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")''')
    st.info("To begin your journey, navigate through the lessons using the sidebar! 👈")

