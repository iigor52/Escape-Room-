import streamlit as st
from datetime import datetime, timedelta

# --- STATION CONFIGURATION ---
STATION_NAME = "Station 1"
CORRECT_ANSWERS = ["B", "A", "C"]  # example answers for 3 questions
CORRECT_CODE = "".join(CORRECT_ANSWERS)  # "BAC" in this example

NEXT_STATION = "Station 2"
NEXT_CODE = "XYZ"  # code for the next station
IS_FINAL = False   # set to True on the last station

# --- SESSION STATE INITIALIZATION ---
if "penalty_until" not in st.session_state:
    st.session_state.penalty_until = None

if "penalty_triggered" not in st.session_state:
    st.session_state.penalty_triggered = False

if "last_code_attempt" not in st.session_state:
    st.session_state.last_code_attempt = ""

if "hint_count" not in st.session_state:
    st.session_state.hint_count = 0

if "hint_text" not in st.session_state:
    st.session_state.hint_text = ""

if "answer_until" not in st.session_state:
    st.session_state.answer_until = None

if "answer_text" not in st.session_state:
    st.session_state.answer_text = ""

if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

# --- HELPER FUNCTIONS ---
def add_penalty_cooldown(seconds: int):
    """Start or extend a penalty timer."""
    now = datetime.utcnow()
    if st.session_state.penalty_until and st.session_state.penalty_until > now:
        st.session_state.penalty_until += timedelta(seconds=seconds)
    else:
        st.session_state.penalty_until = now + timedelta(seconds=seconds)
    st.session_state.penalty_triggered = True  # we used to reset input here

def is_penalty_active() -> bool:
    """Return True if penalty is still running."""
    if not st.session_state.penalty_until:
        return False
    return datetime.utcnow() < st.session_state.penalty_until

def get_penalty_remaining() -> int:
    """Return remaining penalty seconds."""
    if not st.session_state.penalty_until:
        return 0
    remaining = (st.session_state.penalty_until - datetime.utcnow()).total_seconds()
    return max(0, int(remaining))

def get_all_wrong_positions(code_input: str, correct_answers: list):
    """Return indices of wrong answers based on input string and correct answers."""
    wrong = []
    code_input = code_input.upper()
    for i, correct in enumerate(correct_answers):
        if i >= len(code_input):
            wrong.append(i)
        else:
            if code_input[i] != correct:
                wrong.append(i)
    return wrong

# --- PAGE LAYOUT / CSS ---
st.set_page_config(page_title=STATION_NAME, layout="wide")

st.markdown("""
<style>
.question-box {
    background: #ffffff;
    border: 1px solid #e6e6e6;
    padding: 1rem 1.25rem;
    border-radius: 0.5rem;
    margin-bottom: 0.75rem;
}
.success-box {
    background: #ecfff1;
    border-left: 4px solid #17c964;
    padding: 1rem 1.25rem;
    border-radius: 0.5rem;
    margin-bottom: 0.75rem;
}
.answer-box {
    background: #fff5e6;
    border-left: 4px solid #f97316;
    padding: 1rem 1.25rem;
    border-radius: 0.5rem;
    margin-top: 0.75rem;
}
.code-format {
    font-family: monospace;
    font-size: 1.25rem;
    background: #1e293b;
    color: #fff;
    padding: 0.15rem 0.6rem;
    border-radius: 0.35rem;
}
</style>
""", unsafe_allow_html=True)

st.title(STATION_NAME)
st.write("Answer the questions, assemble the code, and verify to move to the next station.")

# --- MAIN CONTENT ---
def main():
    # Questions for this station
    questions = [
        {
            "question": "1. Which of the following is correct for ...?",
            "options": [
                "A) Father with daughter",
                "B) Mother with daughter",
                "C) Brother with brother",
                "D) Sister with brother",
                "E) None of the above"
            ]
        },
        {
            "question": "2. The main reason for ... is?",
            "options": [
                "A) Oxygen transport",
                "B) Coagulation",
                "C) Platelet aggregation",
                "D) Immune modulation",
                "E) None"
            ]
        },
        {
            "question": "3. What is the first step in ... ?",
            "options": [
                "A) Stop infusion",
                "B) Re-check patient data",
                "C) Call physician",
                "D) Document",
                "E) None"
            ]
        }
    ]

    # Show questions
    st.markdown("### ✅ Tasks for this station")
    for i, q in enumerate(questions):
        st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
        st.markdown(f"#### 🔢 Question {i+1}")
        st.write(q["question"])
        for option in q["options"]:
            st.write(f"   {option}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Check penalty status
    penalty_active = is_penalty_active()
    penalty_remaining = get_penalty_remaining()

    # Verification
    st.markdown("### 🎯 Verification and moving to next station")

    col1, col2, col3 = st.columns([2, 1, 1])

    # ✅ HERE IS THE FIXED PART
    with col1:
        if penalty_active:
            # keep last attempted code visible while locked
            input_value = st.session_state.last_code_attempt or ""
            verification_code = st.text_input(
                "🔑 Code:",
                value=input_value,
                disabled=True,
                key="code_input",
                help="🚫 Blocked due to penalty"
            )
            # we don't need the trigger anymore once rendered
            st.session_state.penalty_triggered = False
        else:
            verification_code = st.text_input(
                "🔑 Enter code:",
                placeholder="Three letters (e.g. ABC)",
                max_chars=3,
                key="code_input"
            )

    with col2:
        if penalty_active:
            st.error(f"⏱️ Penalty active: {penalty_remaining}s")
            progress = 1 - (penalty_remaining / 60.0)  # assume max 60s for progress bar
            st.progress(max(0, progress))

    with col3:
        if penalty_active:
            st.button("✅ Verify code", disabled=True)
        else:
            if st.button("✅ Verify code", use_container_width=True):
                st.session_state.last_code_attempt = verification_code

                if verification_code.upper() == CORRECT_CODE:
                    st.balloons()
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)

                    if IS_FINAL:
                        st.success("🎉 CONGRATULATIONS! You have completed all stations!")
                        st.markdown(
                            "Please report to the game master to record your final time and result."
                        )
                    else:
                        st.success("🎉 SUCCESS! You're moving to the next station!")
                        st.markdown("### 🗺️ Continue to the next station:")
                        st.markdown(f"Next station: **{NEXT_STATION}**")
                        st.markdown(
                            f"Code for next station: <span class='code-format'>{NEXT_CODE}</span>",
                            unsafe_allow_html=True
                        )

                    st.markdown('</div>', unsafe_allow_html=True)
                    st.session_state.quiz_completed = True
                    return
                else:
                    st.error("❌ Incorrect code!")
                    add_penalty_cooldown(30)  # fixed 30s penalty for wrong code

    # Help section - ALWAYS AVAILABLE
    st.markdown("### 🆘 Help")
    if penalty_active:
        st.info("ℹ️ Help functions are available even during penalty time")

    help_col1, help_col2 = st.columns(2)

    with help_col1:
        hint_button_text = f"💡 Show incorrect questions (+30s)"
        if st.session_state.hint_count > 0:
            hint_button_text += f" [{st.session_state.hint_count}x]"

        # Help buttons are NEVER disabled
        if st.button(hint_button_text, use_container_width=True, key="hint_btn"):
            # Fixed +30s penalty, cumulative if active
            add_penalty_cooldown(30)
            st.session_state.hint_count += 1

            # Get current code input – now this will NOT be empty during penalty
            current_code_input = verification_code if 'verification_code' in locals() and verification_code else ""
            wrong_positions = get_all_wrong_positions(current_code_input, CORRECT_ANSWERS)

            if not current_code_input:
                hint_text = "Please enter a code first to analyze"
            elif not wrong_positions:
                hint_text = "All entered answers are correct!"
            elif len(wrong_positions) == 1:
                hint_text = f"Question {wrong_positions[0] + 1} is incorrect"
            else:
                q_list = ", ".join([str(i + 1) for i in wrong_positions])
                hint_text = f"Questions {q_list} are incorrect"

            st.session_state.hint_text = hint_text

    with help_col2:
        if st.button("🎯 Reveal correct answer (+60s)", use_container_width=True, key="show_answer_btn"):
            add_penalty_cooldown(60)
            # Show correct code for limited time
            st.session_state.answer_text = f"The correct code is: {CORRECT_CODE}"
            st.session_state.answer_until = datetime.utcnow() + timedelta(seconds=20)

    # Show hint banner if available
    if st.session_state.hint_text:
        st.markdown('<div class="answer-box">', unsafe_allow_html=True)
        st.info(f"💡 **Hint:** {st.session_state.hint_text}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Show answer banner if still in time window
    now = datetime.utcnow()
    if (
        st.session_state.answer_until
        and isinstance(st.session_state.answer_until, datetime)
        and now < st.session_state.answer_until
        and st.session_state.answer_text
    ):
        st.markdown('<div class="answer-box">', unsafe_allow_html=True)
        st.success(f"🎯 **Answer:** {st.session_state.answer_text}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Auto-refresh while penalty active
    if not st.session_state.quiz_completed and is_penalty_active():
        st.experimental_rerun()

if __name__ == "__main__":
    main()
