#chatbot v2
import streamlit as st
import openai
import time
import os

st.set_page_config(page_title='Kaiba AI', page_icon='(-_-)', layout = 'wide')

ASSISTANT_ID='asst_nbcgjebJKUqPXeI8Udu8eDfW'
THREAD_ID='thread_dk7z8qsxikx1z77zezYfDn2l'

api_key = st.secrets.get('OPENAI_API_KEY') or os.environ.get('OPENAI_API_KEY')

if not api_key:
    st.error('OPENAI API Key was not found :(')
    st.stop()
client = openai.OpenAI(api_key=api_key)

# Main Chat interface
st.title('Kaiba AI')

if 'messages' not in st.session_state:
    st.session_state.messages = []
def get_assistant_response(assistant_id, thread_id, user_input):
    try:
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
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything!")
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
    
