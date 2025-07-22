import streamlit as st
import time

st.set_page_config(page_title="Escape Room - Station 1", layout="centered")
st.title("🟩 Station 1: Entry Quiz")

# Access control
start_code = st.text_input("🔐 Please enter password:")

# Normalize input
allowed_codes = ["start1", "start2"]
if start_code:
    if start_code.strip().lower() not in allowed_codes:
        st.error("❌ Wrong password. Please try again.")
        st.stop()
else:
    st.stop()


# Questions and answers
questions = [
    {
        "question": "When substitution therapy with IGG could be recommended?",
        "options": [
            "Multiple myeloma treated with three medications.",
            "Multiple myeloma with low neutrophil number",
            "Multiple myeloma with normal IgG level and infections",
            "Multiple myeloma with affected bones"
        ],
        "answer": "Multiple myeloma with normal IgG level and infections"
    },
    {
        "question": "How higher is the risk of systemic ADRs with IVIG vs SCIG?",
        "options": [
            "Approximately 7 folds higher",
            "Approximately 10 folds higher",
            "Approximately 14 folds higher",
            "The difference is minimal"
        ],
        "answer": "Approximately 10 folds higher"
    },
    {
        "question": "Which group of patients is biggest IGG consumer among PID?",
        "options": [
            "XLA (Bruton's disease) in pediatrics",
            "CVID in adults",
            "Hyper M syndromes + SCID (all ages)",
            "Hyper E syndromes (all ages)"
        ],
        "answer": "CVID in adults"
    },
    {
        "question": "Which dose of SCIG allows to keep the same IgG level after switch from IVIG?",
        "options": [
            "A bit higher than on IVIG",
            "Identical to dose on IVIG",
            "A bit smaller than on IVIG",
            "1,5 folds higher than on IVIG"
        ],
        "answer": "A bit smaller than on IVIG"
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
            st.success("🎉 All questions complete! Your access code to next station is: **AW205**")
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

