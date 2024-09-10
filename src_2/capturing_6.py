# capturing_6
import streamlit as st
def capturingVariables():
    st.header(":six: Capturing Variables")
    st.subheader("Session State")
    st.write("Session state is used to store and persist variables")
    st.subheader("Initializing Values using Session State")
    st.write("There are two ways of initializing a variable")
    st.code('''
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
''')
    st.subheader("Reading and Updating")
    st.write("This code reads the Session state")
    st.code('''
# Read
st.write(st.session_state.key)

# Outputs: value

''')
    st.write("Updates a variable in the session state")
    st.code('''
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API
''')
    st.write("Streamlit will throw a handy exception if an uninitialized variable is accessed:")
    st.code('''st.write(st.session_state['value'])

# Throws an exception!
            ''')
    st.image("https://docs.streamlit.io/images/state_uninitialized_exception.png")
    st.subheader("Deleting session states")
    st.code('''
# Delete a single key-value pair
del st.session_state[key]

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]
    ''')
    st.write("You can also remove them by going to Settings → Clear Cache, followed by Rerunning the app.")
    st.image("https://docs.streamlit.io/images/clear_cache.png")
    st.subheader("Session State and Widget State association")
    st.write("When there is a widget there will also be a session state")
    st.code('''
st.text_input("Your name", key="name")

# This exists now:
st.session_state.name
''')
