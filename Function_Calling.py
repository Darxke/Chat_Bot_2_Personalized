from zoneinfo import ZoneInfo

import openai
import streamlit as st
import json
import time
from datetime import datetime
import pytz

api_key = st.secrets.get('OPENAI_API_KEY')
client = openai.OpenAI(api_key=api_key)

ASSISTANT_ID = 'asst_ucpmCQJVYP8THv8xtiFivSxT'
THREAD_ID = 'thread_Ydh01c39dyUnvKEaHlFPG1LJ'

if 'messages' not in st.session_state:
    st.session_state.messages = []


def get_current_temperature(location: str, unit: str) -> str:
    return f'75*{unit[0]}'


def get_time(location: str) -> str:
    zone = ZoneInfo(location)

    current_time = datetime.now(tzinfo=str(zone))
    return str(current_time)


def get_assistant_response(assistant_id, thread_id, user_input):
    try:
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
        )

        runs = client.beta.threads.runs.list(thread_id=THREAD_ID)
        active_run = next((run for run in runs.data if run.status == "in_progress"), None)

        if active_run:
            while active_run.status == "in_progress":
                time.sleep(1)
                active_run = client.beta.threads.runs.retrieve(
                    thread_id=thread_id,
                    run_id=active_run.id
                )

        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "get_current_temperature",
                        "description": "Get the current temperature for a specific location.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "The city and state, e.g., San Francisco, CA"
                                },
                                "unit": {
                                    "type": "string",
                                    "enum": ["Celsius", "Fahrenheit"],
                                    "description": "The temperature unit to use"
                                }
                            },
                            "required": ["location", "unit"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "get_time",
                        "description": "Gets the current time",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "Get the time of the location"
                                }
                            },
                            "required": ["location"]
                        }
                    }
                },

            ]
        )

        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )
            if run_status.status == 'completed':
                break
            elif run_status.status == 'requires_action':
                tool_outputs = []
                for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
                    if tool_call.function.name == 'get_current_temperature':
                        arguments = json.loads(tool_call.function.arguments)
                        temperature = get_current_temperature(
                            location=arguments['location'],
                            unit=arguments['unit']
                        )

                        tool_outputs.append({
                            'tool_call_id': tool_call.id,
                            'output': json.dumps({'temperature': temperature})
                        })
                    elif tool_call.function.name == 'get_time':
                        arguments = json.loads(tool_call.function.arguments)
                        current_time = get_time(
                            location=arguments['location']
                        )
                        tool_outputs.append({
                            'tool_call_id': tool_call.id,
                            'output': json.dumps({'ti   me': current_time})
                        })

                client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs  # Fixed parameter name
                )

            time.sleep(1)

        messages = client.beta.threads.messages.list(thread_id=thread_id)
        return messages.data[0].content[0].text.value

    except Exception as e:
        st.error(f'Error getting assistant response: {str(e)}')
        return 'I apologize, but I encountered an error. Please try again!'


def main():
    # Add title and description
    st.title("🌤️ Weather Assistant")
    st.markdown("*Ask me about the weather in any location!*")

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

        # Chat input
    if prompt := st.chat_input("Ask about the weather..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner('Getting response'):
                full_response = get_assistant_response(
                    ASSISTANT_ID,
                    THREAD_ID,
                    prompt
                )
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})


if __name__ == '__main__':
    main()
