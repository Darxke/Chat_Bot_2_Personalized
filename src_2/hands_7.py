# hands_7
import streamlit as st
def handsOnActivity():
    st.header(":seven: Hands on Activity")
    st.write("Now it's your turn to create something awsome")
    st.code('''
import streamlit as st
import random

st.title("Guess the number game")

#initialize a variable in a session state
if "secret_num" not in st.session_state:
    st.session_state["secret_num"] = random.randint(1, 100)
    
#Generate a random number between 1-100
#Get the player's guess
user_num = st.number_input("Choose a number between 1-100", min_value = 1, max_value = 100)

if st.button("Guess"):
    if st.session_state.secret_num > user_num:
        st.warning("The secret number is greater than your guess")
    elif st.session_state.secret_num < user_num:
        st.warning("The secert number is less than your guess")
    else:
        st.success("You got it!")
        st.balloons()
''')
