#quiz_10
import streamlit as st
def quiz():
    st.header(":one::zero: Quiz")
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "score" not in st.session_state:
        st.session_state.score = 0
    if "quiz_complete" not in st.session_state:
        st.session_state.quiz_complete = False
    
    quiz_data = [
    {
        "question": "What do you need to import to use st.____",
        "options": ["import streamlit as st", "import st as streamlit", "streamlit import as st", "st import as streamlit"],
        "correct_answer": 0
        
    },
    {
        "question": "What will display the biggest text??",
        "options": ["st.title", "st.header", "st.code", "st.write"],
        "correct_answer": 0
        
    },
    {
        "question": "How do you insert an image",
        "options": ["st.picture", "st.photo", "st.image", "st.wallpaper"],
        "correct_answer": 2
        
    },
    {
        "question": "How do you make a button?",
        "options": ["st.button", "st.insert_button", "st.click", "st.press_button"],
        "correct_answer": 0
        
    },
    {
        "question": "How do you make a check box",
        "options": ["st.check_box", "st.check", "st.box", "st.checkbox"],
        "correct_answer": 3
        
    }
    
]

    #Quiz Logic
    if not st.session_state.quiz_complete:
        question = quiz_data[st.session_state.current_question]
        st.write(f"Question: {st.session_state.current_question + 1} of {len(quiz_data)}")
        st.write(question["question"])
        
        answer = st.radio("Choose your answer", question["options"], key = f"sb_q{st.session_state.current_question}")

        if st.button("sb_Submit"):
            if question["options"].index(answer) == question["correct_answer"]:
                st.success("Nice!")
                st.session_state.score = st.session_state.score + 1
                if st.button("sb_Next"):
                    st.rerun()
                
            else:
                st.error("Wrong")
                st.write(f"The correct answer was :red[{question['options'][question['correct_answer']]}]")
                if st.button("sb_Next"):
                    st.rerun()

            if st.session_state.current_question < len(quiz_data) - 1:
                st.session_state.current_question += 1
            else:
                st.session_state.quiz_complete = True
    else:
        st.success("You finished the quiz!")
        st.write(f"Your final score is {st.session_state.score}/{len(quiz_data)}")
        if st.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_complete = False
            st.rerun()
        

    st.sidebar.write(f"Your current score is {st.session_state.score}/{len(quiz_data)}")
    st.sidebar.write('''
This quiz app demonstrates the use of session_state in several ways:

1. Tracking the current question (st.session_state.current_question)
2. Keeping score (st.session_state.score)
3. Maintaining quiz state (st.session_state.quiz_complete)

These variables persist across reruns, allowing the quiz to maintain its state even when the user interacts with it.
''')
    

    
