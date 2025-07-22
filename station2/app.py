import streamlit as st
import time

st.set_page_config(page_title="Escape Room - Station 2", layout="centered")
st.title("🟨 Station 2: Entry Quiz")

# Access control
start_code = st.text_input("🔐 Enter your start code to begin:")
if start_code:
    if start_code.upper() != "AW205":
        st.warning("🔒 Invalid code. Please enter the correct code from previous station.")
        st.stop()
else:
    st.stop()


# Questions and answers
questions = [
    {
        "question": "For which form of CIDP corticosteroids are not recommended?",
        "options": [
            "All forms",
            "Sensorimotor CIDP",
            "Pure motor CIDP",
            "Single nerve CIDP"
        ],
        "answer": "Pure motor CIDP"
    },
    {
        "question": "When the therapy with IVIG or SCIG should be considered in myeloma?",
        "options": [
            "When the chemotherapy initiated",
            "After first severe infection",
            "After second severe infection",
            "After three or more severe infections"
        ],
        "answer": "After first severe infection"
    },
    {
        "question": "What is the specific limitation for SCIG use in SIDs?",
        "options": [
            "Age",
            "Intensity of chemotherapy",
            "High risk of thrombosis",
            "Advanced cognitive impairment"
        ],
        "answer": "Advanced cognitive impairment"
    },
    {
        "question": "Which patient group is considered the fastest-growing segment for IgG use by 2030?",
        "options": [
            "Neurology patients",
            "Secondary immunodeficiency (SID) patients",
            "Patients with autoimmune myositis",
            "Pediatric Primary Immunodeficiency (PID) patients"
        ],
        "answer": "Secondary immunodeficiency (SID) patients"
    }
]

# Session state
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'delay' not in st.session_state:
    st.session_state.delay = 0
if 'info_text' not in st.session_state:
    st.session_state.info_text = ""

def countdown(seconds):
    if st.session_state.info_text:
        st.markdown(st.session_state.info_text)
    placeholder = st.empty()
    progress = st.progress(0)
    for i in range(seconds, 0, -1):
        placeholder.markdown(f"<h1 style='text-align:center'>⏳ Wait <strong>{i}</strong> seconds...</h1>", unsafe_allow_html=True)
        progress.progress((seconds - i + 1) / seconds)
        time.sleep(1)
    placeholder.empty()
    progress.empty()
    st.session_state.info_text = ""
    st.session_state.delay = 0
    st.rerun()

locked = st.session_state.delay > 0
current_q = questions[st.session_state.question_index]
st.subheader(f"Q{st.session_state.question_index+1}: {current_q['question']}")
choice = st.radio("", current_q['options'], key=f"q{st.session_state.question_index}", disabled=locked)

submitted = st.button("Submit Answer", disabled=locked)

if submitted and not locked:
    if choice == current_q['answer']:
        st.success("✅ Correct!")
        st.session_state.attempts = 0
        st.session_state.info_text = ""
        time.sleep(2)
        if st.session_state.question_index + 1 < len(questions):
            st.session_state.question_index += 1
            st.rerun()
        else:
            st.balloons()
            st.success("🎉 All questions complete! Your access code to next station is: **BR412**")
    else:
        if st.session_state.attempts == 0:
            st.session_state.info_text = "❌ Wrong. Try again in 30 seconds."
            st.session_state.attempts += 1
            st.session_state.delay = 5
            st.rerun()
        else:
            st.session_state.info_text = f"❌ Incorrect again. ✅ Correct answer: **{current_q['answer']}**"
            st.session_state.attempts = 0
            st.session_state.delay = 5
            st.rerun()

if locked:
    countdown(st.session_state.delay)
