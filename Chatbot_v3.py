# Chat Bot V3
import streamlit as st
import openai
import time
import os
from src.homepage import home, bg_home
from src.My_Projects import myProjects
from src.Project_Demonstration import project_Demonstration
from Css_Testing import add_bg_from_local, bg_sideBar
from util import coffee, rainEmojis, my_timeline, cardTab, imageGen, lottie
from st_on_hover_tabs import on_hover_tabs
import base64

# st.set_page_config(page_title='Farming AI', page_icon=':farmer:', layout = 'wide')


ASSISTANT_ID = 'asst_ebiN65dJm6mNDf0ik7v57cwi'
THREAD_ID = 'thread_dk7z8qsxikx1z77zezYfDn2l'

api_key = st.secrets.get('OPENAI_API_KEY') or os.environ.get('OPENAI_API_KEY')
if "bg_change" not in st.session_state:
    st.session_state.bg_change = False
if not api_key:
    st.error('OPENAI API Key was not found :(')
    st.stop()
client = openai.OpenAI(api_key=api_key)

# Main Chat interface

if 'messages' not in st.session_state:
    st.session_state.messages = []


def get_assistant_response(assistant_id, thread_id, user_input):
    try:
        if "create an image" in user_input.lower():
            imageGen(client, user_input)
        else:
            # Add the user's message to the thread
            client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_input
            )
            # Create a run
            run = client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant_id
            )
            # Wait for the run to complete
            while True:
                run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
                if run_status.status == 'completed':
                    break
                time.sleep(1)
            # Retrieve the assistant's messages
            messages = client.beta.threads.messages.list(thread_id=thread_id)

            # Return the latest assistant message
            return messages.data[0].content[0].text.value
    except Exception as e:
        st.error(f"Error getting assistant response: {str(e)}")
        return "I'm sorry, but an error occurred while processing your request."


def display_chatbot():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask me anything! P.S. to create an image just say create an image")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = get_assistant_response(
                ASSISTANT_ID,
                THREAD_ID,
                prompt
            )
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})


def main():
    bg_change = False
    counter = 0
    st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

    with st.sidebar:
        with st.sidebar:
            if st.button("Deploy Change"):
                counter += 1
                if counter % 2 == 0:
                    bg_change = False
                else:
                    bg_change = True
        st.title("Coding Class Presentation")
    with st.sidebar:
        tabs = on_hover_tabs(tabName=["Home", "ChatBot", "My Projects", "Project Demonstration"],
                             iconName=['home', 'chatbot', 'camera', 'person'], default_choice=0)
    if tabs == "Home":
        home()
        my_timeline()
        if bg_change:
            bg_home()
        with st.sidebar:
            if st.button("Secret"):
                bg_home()
                rainEmojis("🏨")
                lottie("https://lottie.host/196ddb8f-8c1e-4fa4-ad54-7475a53ccae1/Pls0SIUzel.json")
            coffee()

    if tabs == "ChatBot":
        st.markdown("<h1 style='text-align: center; color: black;'>🤖 ChatBot AI</h1>", unsafe_allow_html=True)
        with st.sidebar:
            if st.button("Secret"):
                rainEmojis("🤖")
                bg_sideBar("#cdd67c")
                add_bg_from_local('./images/ligth color.jpg')
                lottie("https://lottie.host/94c95a1d-e8e6-44ad-9457-cc03b47bdb6b/Lt1MX4XEEH.json")

        if bg_change:
            bg_sideBar("#cdd67c")
            add_bg_from_local('./images/ligth color.jpg')
        display_chatbot()
    if tabs == "My Projects":
        with st.sidebar:
            if st.button("Secret"):
                add_bg_from_local('./images/Spotlight.jpg')
                bg_sideBar("#000000")
                lottie("https://lottie.host/05ba2cb6-6dac-4e2b-b18e-dcec8adff357/cN4cpyXRzG.json")
        if bg_change:
            add_bg_from_local('./images/Spotlight.jpg')
            bg_sideBar("#000000")

        myProjects()
    if tabs == "Project Demonstration":
        project_Demonstration()



if __name__ == "__main__":
    main()
