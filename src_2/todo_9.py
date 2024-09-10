#todo_9
import streamlit as st
def toDoList():
    if "todos" not in st.session_state:
        st.session_state.todos = []

    todo = st.text_input("Please enter a todo item")

    if st.button("Add"):
        st.session_state.todos.append(todo)

    st.header(f":nine: ToDo List")

    for i , todo in enumerate(st.session_state.todos):
        st.write(f"{i+1}. {todo}")
