import streamlit as st
from datetime import datetime, timedelta
from typing import Optional, List

# NOTE: Generator će ovdje ubaciti konkretne podatke za svaku stanicu.
# Ostavite ovu liniju kakva jest i neka generator zamijeni cijeli blok ispod.
STATION_DATA = {
    "station_number": 7,
    "station_name": "Escaping from the immunotherapy challenges - Station 7",
    "groups": {
        "group1": {
            "name": "Group 1",
            "next_station": None,
            "next_code": "IBTIMM12",
            "is_final": True,
            "questions": [
                {
                    "question": "Which of the following statements about SCIG is TRUE in the context of SID management?",
                    "options": [
                        "A) SCIG is preferred over IVIG in acute infection settings",
                        "B) SCIG is rarely used due to higher systemic side effects",
                        "C) SCIG is contraindicated in patients with MM",
                        "D) SCIG allows more stable IgG trough levels and home administration",
                        "E) SCIG has a higher rate of anaphylactic reactions than IVIG"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which class of new treatment options is an opportunity for IVIG/SCIG as they may induce infections due to immune modulation?",
                    "options": [
                        "A) FcRn inhibitors",
                        "B) Complement inhibitors",
                        "C) Bi-specific T-cell engagers (BiTEs)",
                        "D) Gene therapy",
                        "E) RNA interference therapies"
                    ],
                    "correct": "C"
                },
                {
                    "question": "What’s the best drink after a busy day?",
                    "options": [
                        "A) Coca Cola",
                        "B) Water",
                        "C) Prosecco",
                        "D) Beer",
                        "E) Orange juice"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group2": {
            "name": "Group 2",
            "next_station": 1,
            "next_code": "VB456",
            "is_final": False,
            "questions": [
                {
                    "question": "Which of the following statements about SCIG is TRUE in the context of SID management?",
                    "options": [
                        "A) SCIG is preferred over IVIG in acute infection settings",
                        "B) SCIG is rarely used due to higher systemic side effects",
                        "C) SCIG is contraindicated in patients with MM",
                        "D) SCIG allows more stable IgG trough levels and home administration",
                        "E) SCIG has a higher rate of anaphylactic reactions than IVIG"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which class of new treatment options is an opportunity for IVIG/SCIG as they may induce infections due to immune modulation?",
                    "options": [
                        "A) FcRn inhibitors",
                        "B) Complement inhibitors",
                        "C) Bi-specific T-cell engagers (BiTEs)",
                        "D) Gene therapy",
                        "E) RNA interference therapies"
                    ],
                    "correct": "C"
                },
                {
                    "question": "What’s the best drink after a busy day?",
                    "options": [
                        "A) Coca Cola",
                        "B) Water",
                        "C) Prosecco",
                        "D) Beer",
                        "E) Orange juice"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group3": {
            "name": "Group 3",
            "next_station": 1,
            "next_code": "QR789",
            "is_final": False,
            "questions": [
                {
                    "question": "Which of the following statements about SCIG is TRUE in the context of SID management?",
                    "options": [
                        "A) SCIG is preferred over IVIG in acute infection settings",
                        "B) SCIG is rarely used due to higher systemic side effects",
                        "C) SCIG is contraindicated in patients with MM",
                        "D) SCIG allows more stable IgG trough levels and home administration",
                        "E) SCIG has a higher rate of anaphylactic reactions than IVIG"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which class of new treatment options is an opportunity for IVIG/SCIG as they may induce infections due to immune modulation?",
                    "options": [
                        "A) FcRn inhibitors",
                        "B) Complement inhibitors",
                        "C) Bi-specific T-cell engagers (BiTEs)",
                        "D) Gene therapy",
                        "E) RNA interference therapies"
                    ],
                    "correct": "C"
                },
                {
                    "question": "What’s the best drink after a busy day?",
                    "options": [
                        "A) Coca Cola",
                        "B) Water",
                        "C) Prosecco",
                        "D) Beer",
                        "E) Orange juice"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group4": {
            "name": "Group 4",
            "next_station": 1,
            "next_code": "ZX012",
            "is_final": False,
            "questions": [
                {
                    "question": "Which of the following statements about SCIG is TRUE in the context of SID management?",
                    "options": [
                        "A) SCIG is preferred over IVIG in acute infection settings",
                        "B) SCIG is rarely used due to higher systemic side effects",
                        "C) SCIG is contraindicated in patients with MM",
                        "D) SCIG allows more stable IgG trough levels and home administration",
                        "E) SCIG has a higher rate of anaphylactic reactions than IVIG"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which class of new treatment options is an opportunity for IVIG/SCIG as they may induce infections due to immune modulation?",
                    "options": [
                        "A) FcRn inhibitors",
                        "B) Complement inhibitors",
                        "C) Bi-specific T-cell engagers (BiTEs)",
                        "D) Gene therapy",
                        "E) RNA interference therapies"
                    ],
                    "correct": "C"
                },
                {
                    "question": "What’s the best drink after a busy day?",
                    "options": [
                        "A) Coca Cola",
                        "B) Water",
                        "C) Prosecco",
                        "D) Beer",
                        "E) Orange juice"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group5": {
            "name": "Group 5",
            "next_station": 1,
            "next_code": "MN345",
            "is_final": False,
            "questions": [
                {
                    "question": "Which of the following statements about SCIG is TRUE in the context of SID management?",
                    "options": [
                        "A) SCIG is preferred over IVIG in acute infection settings",
                        "B) SCIG is rarely used due to higher systemic side effects",
                        "C) SCIG is contraindicated in patients with MM",
                        "D) SCIG allows more stable IgG trough levels and home administration",
                        "E) SCIG has a higher rate of anaphylactic reactions than IVIG"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which class of new treatment options is an opportunity for IVIG/SCIG as they may induce infections due to immune modulation?",
                    "options": [
                        "A) FcRn inhibitors",
                        "B) Complement inhibitors",
                        "C) Bi-specific T-cell engagers (BiTEs)",
                        "D) Gene therapy",
                        "E) RNA interference therapies"
                    ],
                    "correct": "C"
                },
                {
                    "question": "What’s the best drink after a busy day?",
                    "options": [
                        "A) Coca Cola",
                        "B) Water",
                        "C) Prosecco",
                        "D) Beer",
                        "E) Orange juice"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group6": {
            "name": "Group 6",
            "next_station": 1,
            "next_code": "KL678",
            "is_final": False,
            "questions": [
                {
                    "question": "Which of the following statements about SCIG is TRUE in the context of SID management?",
                    "options": [
                        "A) SCIG is preferred over IVIG in acute infection settings",
                        "B) SCIG is rarely used due to higher systemic side effects",
                        "C) SCIG is contraindicated in patients with MM",
                        "D) SCIG allows more stable IgG trough levels and home administration",
                        "E) SCIG has a higher rate of anaphylactic reactions than IVIG"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which class of new treatment options is an opportunity for IVIG/SCIG as they may induce infections due to immune modulation?",
                    "options": [
                        "A) FcRn inhibitors",
                        "B) Complement inhibitors",
                        "C) Bi-specific T-cell engagers (BiTEs)",
                        "D) Gene therapy",
                        "E) RNA interference therapies"
                    ],
                    "correct": "C"
                },
                {
                    "question": "What’s the best drink after a busy day?",
                    "options": [
                        "A) Coca Cola",
                        "B) Water",
                        "C) Prosecco",
                        "D) Beer",
                        "E) Orange juice"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group7": {
            "name": "Group 7",
            "next_station": 1,
            "next_code": "PW901",
            "is_final": False,
            "questions": [
                {
                    "question": "Which of the following statements about SCIG is TRUE in the context of SID management?",
                    "options": [
                        "A) SCIG is preferred over IVIG in acute infection settings",
                        "B) SCIG is rarely used due to higher systemic side effects",
                        "C) SCIG is contraindicated in patients with MM",
                        "D) SCIG allows more stable IgG trough levels and home administration",
                        "E) SCIG has a higher rate of anaphylactic reactions than IVIG"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which class of new treatment options is an opportunity for IVIG/SCIG as they may induce infections due to immune modulation?",
                    "options": [
                        "A) FcRn inhibitors",
                        "B) Complement inhibitors",
                        "C) Bi-specific T-cell engagers (BiTEs)",
                        "D) Gene therapy",
                        "E) RNA interference therapies"
                    ],
                    "correct": "C"
                },
                {
                    "question": "What’s the best drink after a busy day?",
                    "options": [
                        "A) Coca Cola",
                        "B) Water",
                        "C) Prosecco",
                        "D) Beer",
                        "E) Orange juice"
                    ],
                    "correct": "B"
                }
            ]
        }
    },
    "access_codes": {
        "QW789": "group1",
        "ER012": "group2",
        "TY345": "group3",
        "UI678": "group4",
        "OP901": "group5",
        "AS234": "group6",
        "DF567": "group7"
    }
}

# App config
st.set_page_config(
    page_title=f"🧬 Escape room - {STATION_DATA['station_name']}",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# UI styles
st.markdown("""
<style>
.block-container {padding-top: 2rem; padding-bottom: 2rem;}
h1, h2, h3 {color: #1E88E5;}
.stButton button {
  background-color:#1E88E5; color:white; border-radius:5px;
  height:3em; font-weight:bold;
}
.hint-box {background:#E3F2FD; border-left:5px solid #1E88E5; padding:15px; margin:15px 0; border-radius:5px;}
.answer-box {background:#E8F5E9; border-left:5px solid #4CAF50; padding:15px; margin:15px 0; border-radius:5px;}
.success-box {background:#E8F5E9; border-left:5px solid #4CAF50; padding:20px; margin-bottom:20px;}
.question-box {background:#F5F5F5; border-radius:5px; padding:15px; margin-bottom:15px;}
.code-format {font-family:monospace; font-size:1.1em; letter-spacing:2px; background:#F5F5F5;
  padding:4px 8px; border-radius:4px; border:1px solid #DDD;}
.timer-display {color:#F44336; font-weight:bold; margin-top:8px; font-size:1.05em;}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Session helpers
# ---------------------------

def initialize_session():
    defaults = {
        'group_id': None,
        'group_name': None,
        'start_time': None,
        'penalty_end_time': None,
        'total_penalties': 0,
        'hint_count': 0,
        'answer_count': 0,
        'last_code_attempt': "",
        'access_code': "",
        'hint_until': None,
        'answer_until': None,
        'hint_text': "",
        'answer_text': "",
        'revealed_answers': set(),
        'quiz_completed': False,
        'is_final': False,
        'questions': [],
        'next_station': None,
        'next_code': "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def is_penalty_active() -> bool:
    end = st.session_state.penalty_end_time
    return bool(end and datetime.now() < end)

def get_penalty_remaining() -> int:
    if not is_penalty_active(): return 0
    return max(0, int((st.session_state.penalty_end_time - datetime.now()).total_seconds()))

def add_penalty_cooldown(seconds: int):
    now = datetime.now()
    st.session_state.total_penalties += seconds
    end = st.session_state.penalty_end_time
    if end is None or now >= end:
        st.session_state.penalty_end_time = now + timedelta(seconds=seconds)
    else:
        remaining = (end - now).total_seconds()
        st.session_state.penalty_end_time = now + timedelta(seconds=remaining + seconds)

# ---------------------------
# Quiz helpers
# ---------------------------

def get_all_wrong_positions(code_attempt: str, correct_answers: List[str]) -> List[int]:
    if not code_attempt: return []
    code_upper = code_attempt.upper()
    wrong = []
    for i in range(min(len(code_upper), len(correct_answers))):
        if code_upper[i] != correct_answers[i]:
            wrong.append(i)
    return wrong

def get_next_unrevealed_wrong_position(code_attempt: str, correct_answers: List[str]) -> Optional[int]:
    if not code_attempt: return None
    wrong_positions = get_all_wrong_positions(code_attempt, correct_answers)
    if not isinstance(st.session_state.revealed_answers, set):
        st.session_state.revealed_answers = set(st.session_state.revealed_answers)
    for pos in wrong_positions:
        if pos not in st.session_state.revealed_answers:
            return pos
    return None

def show_welcome():
    st.markdown(f"## 👋 Welcome to {STATION_DATA['station_name']}")
    st.markdown("""
1. Answer all questions
2. Convert answers into a code (e.g. ABC)
3. Enter the code to proceed
4. Help is available but adds time penalties
""")
    st.markdown("Format: <span class='code-format'>XY123</span>", unsafe_allow_html=True)

# ---------------------------
# Main
# ---------------------------

def main():
    initialize_session()

    # Access gate
    if st.session_state.group_id is None:
        show_welcome()
        col1, col2 = st.columns([3, 1])
        with col1:
            access_code = st.text_input(
                "Access code:",
                value=st.session_state.access_code,
                key="access_code_input",
                placeholder="XY123"
            )
        with col2:
            if st.button("Start", use_container_width=True):
                st.session_state.access_code = access_code
                code_upper = (access_code or "").strip().upper()

                match = None
                for stored_code, group_key in STATION_DATA["access_codes"].items():
                    if stored_code.strip().upper() == code_upper:
                        match = stored_code
                        break

                if match:
                    gid = STATION_DATA["access_codes"][match]
                    gdata = STATION_DATA["groups"][gid]

                    st.session_state.group_id = gid
                    st.session_state.group_name = gdata["name"]
                    st.session_state.start_time = datetime.now()
                    st.session_state.questions = gdata["questions"]
                    st.session_state.next_station = gdata["next_station"]
                    st.session_state.next_code = gdata["next_code"]
                    st.session_state.is_final = gdata["is_final"]

                    st.success(f"Welcome, {gdata['name']}!")
                    st.rerun()
                else:
                    st.error("Invalid access code")
        return

    # Loaded group
    gdata = STATION_DATA["groups"][st.session_state.group_id]
    questions = st.session_state.questions
    correct_answers = [q["correct"] for q in questions]
    correct_code = "".join(correct_answers)

    # Header
    st.title(STATION_DATA["station_name"])
    st.subheader(st.session_state.group_name)

    if st.session_state.total_penalties > 0:
        st.metric("Total penalties", f"+{st.session_state.total_penalties}s")

    # Body
    if not st.session_state.quiz_completed:
        st.markdown("### Questions")
        for i, q in enumerate(questions):
            st.markdown('<div class="question-box">', unsafe_allow_html=True)
            st.markdown(f"**Q{i+1}.** {q['question']}")
            for opt in q["options"]:
                st.write(opt)
            st.markdown('</div>', unsafe_allow_html=True)

        penalty_active = is_penalty_active()
        remaining = get_penalty_remaining()

        # Verification
        st.markdown("### Code Verification")
        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            if penalty_active:
                verification_code = st.text_input(
                    "Code (locked during penalty):",
                    value=st.session_state.last_code_attempt,
                    disabled=True,
                    key="code_input",
                    help="Wait for the countdown"
                )
            else:
                verification_code = st.text_input(
                    "Enter code:",
                    value=st.session_state.last_code_attempt,
                    max_chars=3,
                    key="code_input"
                )
                # Update attempt while typing (only when not penalized)
                st.session_state.last_code_attempt = verification_code

        with col2:
            if penalty_active:
                st.markdown(f'<div class="timer-display">⏳ {remaining}s</div>', unsafe_allow_html=True)
                progress = 1 - (remaining / 60) if remaining <= 60 else 0
                st.progress(max(0, progress))

        with col3:
            if st.button("Verify", use_container_width=True, disabled=penalty_active):
                st.session_state.last_code_attempt = verification_code
                if (verification_code or "").upper() == correct_code:
                    st.balloons()
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    if st.session_state.is_final:
                        st.success("Final station complete!")
                        st.markdown("Your completion code:")
                        st.markdown(f"<span class='code-format'>{st.session_state.next_code}</span>", unsafe_allow_html=True)
                    else:
                        st.success("Correct! Proceed to next station.")
                        st.markdown(f"Next station: **{st.session_state.next_station}**")
                        st.markdown(f"Next code: <span class='code-format'>{st.session_state.next_code}</span>", unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.session_state.quiz_completed = True
                else:
                    st.error("Incorrect code")
                    add_penalty_cooldown(30)
                    st.warning("+30s penalty added")

        # Help
        st.markdown("### Help")
        if penalty_active:
            st.info("Help is available during penalty (adds extra time).")

        h1, h2 = st.columns(2)

        with h1:
            txt = "💡 Show incorrect questions (+30s)"
            if st.session_state.hint_count > 0:
                txt += f" [{st.session_state.hint_count}x]"
            if st.button(txt, use_container_width=True):
                add_penalty_cooldown(30)
                st.session_state.hint_count += 1
                current_code = (st.session_state.last_code_attempt or "").strip()
                wrong_positions = get_all_wrong_positions(current_code, correct_answers)

                if not current_code:
                    st.session_state.hint_text = "Enter a code first"
                elif not wrong_positions:
                    st.session_state.hint_text = "All letters correct"
                elif len(wrong_positions) == 1:
                    st.session_state.hint_text = f"Question {wrong_positions[0] + 1} incorrect"
                else:
                    st.session_state.hint_text = "Questions " + ", ".join(str(p + 1) for p in wrong_positions) + " incorrect"

                st.session_state.hint_until = datetime.now() + timedelta(seconds=30)

        with h2:
            txt = "🎯 Reveal one correct answer (+60s)"
            if st.session_state.answer_count > 0:
                txt += f" [{st.session_state.answer_count}x]"
            if st.button(txt, use_container_width=True):
                add_penalty_cooldown(60)
                st.session_state.answer_count += 1
                current_code = (st.session_state.last_code_attempt or "").strip()
                nxt = get_next_unrevealed_wrong_position(current_code, correct_answers)

                if not current_code:
                    ans = "Enter a code first"
                elif nxt is None:
                    wrong_all = get_all_wrong_positions(current_code, correct_answers)
                    if not wrong_all:
                        ans = "All answers already correct"
                    else:
                        ans = "All incorrect positions already revealed"
                else:
                    st.session_state.revealed_answers.add(nxt)
                    ans = f"Question {nxt + 1}: correct letter is {correct_answers[nxt]}"

                st.session_state.answer_text = ans
                st.session_state.answer_until = datetime.now() + timedelta(seconds=30)

        now = datetime.now()
        if st.session_state.hint_text and st.session_state.hint_until and now < st.session_state.hint_until:
            st.markdown('<div class="hint-box">', unsafe_allow_html=True)
            st.info(st.session_state.hint_text)
            st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.answer_text and st.session_state.answer_until and now < st.session_state.answer_until:
            st.markdown('<div class="answer-box">', unsafe_allow_html=True)
            st.success(st.session_state.answer_text)
            st.markdown('</div>', unsafe_allow_html=True)

        # Light auto-refresh for the countdown
        if penalty_active:
            st.experimental_autorefresh(interval=1000, key="penalty_autorefresh")

if __name__ == "__main__":
    main()