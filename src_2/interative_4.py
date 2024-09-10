# interactive _ 4
import streamlit as st
def interativeApp():
    st.header(":four: Simple Interative App")
    st.subheader("Let's create a basic calculator")
    num1 = st.number_input("Please enter your first number", value = 0)
    num2 = st.number_input("Please enter you second number", value = 0)
    operation = st.selectbox("Choose your operation", ["+", "-", "*", "/"])
    result = 0
    if st.button("Calculate"):
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Can not divide by zero")
                quit()
        st.success(result)
