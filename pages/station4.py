import streamlit as st
from datetime import datetime, timedelta
import time
import os
import socket
from typing import Optional, List

def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))  # Bind to a free port provided by the OS
    port = s.getsockname()[1]
    s.close()
    return port

# Set Streamlit to use a free port
os.environ["STREAMLIT_SERVER_PORT"] = str(find_free_port())

STATION_DATA = {
    "station_number": 4,
    "station_name": "ICU Escape Room - Station 4",
    "groups": {
        "group1": {
            "name": "Group 1",
            "next_station": 5,
            "next_code": "IJ123",
            "is_final": False,
            "questions": [
                {
                    "question": "Which rare, non-enveloped virus is NAT-tested in the manufacturing pool for OctaplasLG, as part of its pathogen safety protocol?",
                    "options": [
                        "A) Zika virus",
                        "B) Hepatitis E virus (HEV)",
                        "C) Epstein-Barr virus",
                        "D) Dengue virus",
                        "E) Poliovirus"
                    ],
                    "correct": "B"
                },
                {
                    "question": "Why it is important to normalise fibrinogen level before considering any other intervention with coagulation factors?",
                    "options": [
                        "A) All tests in routine practice reflecting factors activity are fibrinogen dependent",
                        "B) Coagulation factors cannot build good quality thrombus without fibrinogen",
                        "C) With low fibrinogen risk of infections is higher",
                        "D) All of the above",
                        "E) A and B"
                    ],
                    "correct": "E"
                },
                {
                    "question": "What is the main risk associated with transfusion of FFP after CPB, compared to use of coagulation factor concentrates?",
                    "options": [
                        "A) Increased incidence of transfusion-related acute lung injury (TRALI)",
                        "B) Greater risk of transfusion-associated circulatory overload (TACO) and dilutional coagulopathy",
                        "C) Higher frequency of allergic transfusion reactions",
                        "D) Risk of hepatitis E transmission",
                        "E) All of the above"
                    ],
                    "correct": "E"
                }
            ]
        },
        "group2": {
            "name": "Group 2",
            "next_station": 5,
            "next_code": "IJ456",
            "is_final": False,
            "questions": [
                {
                    "question": "Why is monitoring of ATIII levels important in children with acute lymphoblastic leukemia (ALL) receiving asparaginase?",
                    "options": [
                        "A) To decide when to transfuse red blood cells",
                        "B) To guide prophylaxis or treatment of thrombosis",
                        "C) To predict risk of febrile neutropenia",
                        "D) To adjust platelet transfusion thresholds",
                        "E) To influence on degree of inflammation"
                    ],
                    "correct": "B"
                },
                {
                    "question": "Which two conditions require anticoagulants reversal most frequently?",
                    "options": [
                        "A) Trauma and urgent cardiac surgery",
                        "B) Intracranial haemorrhage and gastrointestinal bleeding",
                        "C) Trauma and gastrointestinal bleeding",
                        "D) Urgent cardiac surgery and dental surgery",
                        "E) Intracranial haemorrhage and urological surgery"
                    ],
                    "correct": "B"
                },
                {
                    "question": "Regarding the use of albumin in acute kidney injury (AKI) in cirrhosis, which statement reflects the current evidence and best practice?",
                    "options": [
                        "A) Albumin is mainly used as a drug for widening blood vessels (vasodilation)",
                        "B) Albumin should be given at 1 g/kg (up to 100 g) over 48 hours to help distinguish HRS from pre-renal (dehydration-related) AKI",
                        "C) Only very small albumin doses (<10 g) should be given",
                        "D) Albumin should not be used in patients with AKI and cirrhosis",
                        "E) Albumin should be used only if diuretics failed"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group3": {
            "name": "Group 3",
            "next_station": 5,
            "next_code": "IJ789",
            "is_final": False,
            "questions": [
                {
                    "question": "A 72-year-old on apixaban presents with major GI bleeding. Anti-Xa activity in blood is highly elevated. What is the first line treatment according to European guidelines 2024?",
                    "options": [
                        "A) Andexanet alfa",
                        "B) Four factors PCC",
                        "C) Watch and wait approach",
                        "D) Andexanet alfa or PCC without priority",
                        "E) Protamine sulphate"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which rare virus circulating in Europe is sensitive to S/D inactivation used in OctaplasLG manufacturing process?",
                    "options": [
                        "A) Zika virus",
                        "B) Poliovirus",
                        "C) Enterovirus",
                        "D) West Nile virus",
                        "E) Hepatitis E virus (HEV)"
                    ],
                    "correct": "D"
                },
                {
                    "question": "Which treatment is superior for majority of cardiac surgery patients (except of \"critical\") according to results of FIBRES randomized study?",
                    "options": [
                        "A) Cryoprecipitate",
                        "B) Fibrinogen concentrate",
                        "C) No difference",
                        "D) FFP",
                        "E) Platelets"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group4": {
            "name": "Group 4",
            "next_station": 5,
            "next_code": "IJ012",
            "is_final": False,
            "questions": [
                {
                    "question": "In pediatric patients with newly diagnosed acute lymphoblastic leukemia (ALL), what is the most likely cause of decreased antithrombin III (ATIII) levels during induction therapy?",
                    "options": [
                        "A) Hepatic synthesis impairment due to corticosteroids",
                        "B) Asparaginase treatment side effect",
                        "C) Renal excretion due to tumour lysis",
                        "D) Vitamin K deficiency",
                        "E) Need to use high dosages of heparin"
                    ],
                    "correct": "B"
                },
                {
                    "question": "What is one of recommended early interventions in case of severe traumatic bleeding according to European guidelines?",
                    "options": [
                        "A) Whole blood",
                        "B) Red blood cells and platelets",
                        "C) FFP and platelets",
                        "D) Red blood cells and colloids",
                        "E) Red blood cells and fibrinogen"
                    ],
                    "correct": "E"
                },
                {
                    "question": "An 81-year-old on dabigatran presents with life-threatening gastric bleeding. Idarucizumab is not available. What is next step according to European guidelines 2024?",
                    "options": [
                        "A) Administer 5 mg IV vitamin K",
                        "B) Give 4-factor PCC (Octaplex)",
                        "C) Infuse andexanet alfa",
                        "D) Give protamine sulphate",
                        "E) Watch and wait approach"
                    ],
                    "correct": "B"
                }
            ]
        },
        "group5": {
            "name": "Group 5",
            "next_station": None,
            "next_code": "FINAL556",
            "is_final": True,
            "questions": [
                {
                    "question": "Is transmission of Human Immunodeficiency Virus (HIV) has ever been reported for any type of inactivated plasma?",
                    "options": [
                        "A) No",
                        "B) Yes, for single bag inactivated plasma possibly due to human error",
                        "C) Yes, for S/D treated plasma due to high viral load in source plasma",
                        "D) Yes, for each type of inactivated plasma with low frequency",
                        "E) Yes, this is common"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Which important safety concern was registered in randomized Annexa-I study (Andexanet alfa vs usual care mainly with PCC)?",
                    "options": [
                        "A) Higher thrombotic risk for PCC",
                        "B) Higher thrombotic risk for andexanet alfa",
                        "C) High rate of allergic reaction on PCC",
                        "D) High rate of allergic reaction on andexanet alfa",
                        "E) Equal safety with higher efficacy of PCC"
                    ],
                    "correct": "B"
                },
                {
                    "question": "What is a mechanism by which OctaplasLG minimizes the risk of non-enveloped viral transmission (such as HAV and parvovirus B19)?",
                    "options": [
                        "A) S/D treatment alone",
                        "B) High-dose gamma irradiation",
                        "C) Filtration and presence of neutralizing antibodies from pooled donations",
                        "D) Freezing at -40\u00b0C",
                        "E) Pasteurization"
                    ],
                    "correct": "C"
                }
            ]
        },
        "group6": {
            "name": "Group 6",
            "next_station": 5,
            "next_code": "IJ678",
            "is_final": False,
            "questions": [
                {
                    "question": "A patient with decompensated cirrhosis undergoes large-volume paracentesis with removal of 6 Liters of ascites. What is the recommended management to prevent post-paracentesis circulatory dysfunction (PICD)?",
                    "options": [
                        "A) Infuse 6\u20138 g albumin per litre removed",
                        "B) Infuse normal saline, 1 L per 2 L drained",
                        "C) Start vasopressors preemptively",
                        "D) No intervention needed unless symptoms develop",
                        "E) Start infusion of any available colloid"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Which outcomes were registered in recent randomized study FARES-II (PCC (Octaplex) vs FFP) in cardiac surgery?",
                    "options": [
                        "A) Better efficacy of PCC, lower rate of acute kidney injury (AKI) in PCC group, similar rate of thrombosis",
                        "B) Better efficacy of PCC, equal safety",
                        "C) Non-inferiority of PCC vs FFP in efficacy and safety",
                        "D) Better efficacy of PCC with slightly higher rate of thrombotic complications",
                        "E) Better efficacy of PCC with slightly higher rate of AKI"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Which treatment should be given first in moderate post-bypass (CPB) bleeding when fibrinogen level is 1.1 g/L, platelets number is 54 G/L?",
                    "options": [
                        "A) Fibrinogen and platelets",
                        "B) Fibrinogen and PCC",
                        "C) FFP and platelets",
                        "D) Fibrinogen only",
                        "E) Platelets only"
                    ],
                    "correct": "A"
                }
            ]
        },
        "group7": {
            "name": "Group 7",
            "next_station": 5,
            "next_code": "IJ901",
            "is_final": False,
            "questions": [
                {
                    "question": "What is a key practical advantage of using fibryga compared to cryoprecipitate or FFP in the management of active bleeding?",
                    "options": [
                        "A) Opportunity to store the product in the normal refrigerator (+5 \u2013 +10)",
                        "B) Big additional infusion volume to restore fluid balance",
                        "C) Exact dosing, rapid preparation and administration, and minimized volume load",
                        "D) Higher content of additional coagulation factors (e.g., factor XIII, vWF)",
                        "E) Higher content of total protein"
                    ],
                    "correct": "C"
                },
                {
                    "question": "In real-world health system data, frequency of which adverse event is reduced after switching from FFP to OctaplasLG?",
                    "options": [
                        "A) TACO",
                        "B) Bacterial infection",
                        "C) Allergic and anaphylactic reactions",
                        "D) Hypercalcaemia",
                        "E) Hypoproteinaemia"
                    ],
                    "correct": "C"
                },
                {
                    "question": "Is risk of thrombosis with fibrinogen concentrate higher than with other treatments used in randomized studies?",
                    "options": [
                        "A) Yes, slightly higher only in comparison to placebo",
                        "B) Yes, only in postpartum haemorrhage",
                        "C) Yes, if fibrinogen level was assessed poorly",
                        "D) No",
                        "E) Yes, in neonates only"
                    ],
                    "correct": "D"
                }
            ]
        }
    },
    "access_codes": {
        "GH123": "group1",
        "GH456": "group2",
        "GH789": "group3",
        "GH012": "group4",
        "GH345": "group5",
        "GH678": "group6",
        "GH901": "group7"
    }
}

# Application configuration
st.set_page_config(
    page_title=f"🧬 Escape room - {STATION_DATA['station_name']}",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for improved appearance
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #1E88E5;
    }
    .stButton button {
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
    }
    .hint-box {
        background-color: #E3F2FD;
        border-left: 5px solid #1E88E5;
        padding: 10px;
    }
    .answer-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 10px;
    }
    .timeout-box {
        background-color: #FFEBEE;
        border-left: 5px solid #F44336;
        padding: 20px;
        margin-bottom: 20px;
    }
    .success-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 20px;
        margin-bottom: 20px;
    }
    .question-box {
        background-color: #F5F5F5;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .code-format {
        font-family: monospace;
        font-size: 1.2em;
        letter-spacing: 2px;
        background-color: #F5F5F5;
        padding: 5px 10px;
        border-radius: 4px;
        border: 1px solid #DDD;
    }
    .timer-display {
        color: #F44336;
        font-weight: bold;
        margin-top: 8px;
        font-size: 1.1em;
    }
    .penalty-warning {
        background-color: #FFF3E0;
        border-left: 4px solid #FF9800;
        padding: 10px;
        margin: 10px 0;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Session and penalty helpers
# ---------------------------

def initialize_session():
    """Initialize session variables"""
    defaults = {
        'group_id': None,
        'group_name': None,
        'start_time': None,

        # Penalty model
        'penalty_end_time': None,
        'total_penalties': 0,
        'penalty_triggered': False,

        # Help usage counters (for button label)
        'hint_count': 0,
        'answer_count': 0,

        # Previous input
        'last_code_attempt': "",
        'access_code': "",

        # One-shot banners (TTL)
        'hint_until': None,
        'answer_until': None,
        'hint_text': "",
        'answer_text': "",

        'quiz_completed': False,
        
        # For auto-refresh optimization
        'last_penalty_check': None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def is_penalty_active():
    """Check if penalty is active"""
    end = st.session_state.penalty_end_time
    if end is None:
        return False
    return datetime.now() < end


def get_penalty_remaining():
    """Get remaining penalty time in seconds"""
    if not is_penalty_active():
        return 0
    return int((st.session_state.penalty_end_time - datetime.now()).total_seconds())


def add_penalty_cooldown(seconds: int):
    """
    Adds a fixed penalty amount, cumulatively.
    If a penalty is already active, extend from its end.
    """
    now = datetime.now()
    st.session_state.total_penalties += seconds

    if st.session_state.penalty_end_time is None or now >= st.session_state.penalty_end_time:
        st.session_state.penalty_end_time = now + timedelta(seconds=seconds)
    else:
        current_remaining = (st.session_state.penalty_end_time - now).total_seconds()
        new_total = current_remaining + seconds
        st.session_state.penalty_end_time = now + timedelta(seconds=new_total)

    # signal input reset
    st.session_state.penalty_triggered = True


# ---------------------------
# Quiz helpers
# ---------------------------

def analyze_code_attempt(code_attempt, questions):
    """Analyze entered code and provide feedback (may return multi-question text)"""
    if not code_attempt:
        return "No code entered"

    correct_answers = [q["correct"] for q in questions]
    correct_code = "".join(correct_answers)
    code_upper = code_attempt.upper()

    if len(code_upper) != 3:  # 3 questions
        return f"Code must have 3 letters (you entered {len(code_upper)})"

    if code_upper == correct_code:
        return "The code is CORRECT! ✅"

    wrong_positions = []
    for i in range(min(len(code_upper), 3)):
        if i < len(correct_answers) and code_upper[i] != correct_answers[i]:
            wrong_positions.append(i + 1)

    if len(wrong_positions) == 1:
        return f"Question {wrong_positions[0]} is incorrect"
    else:
        position_list = " & ".join(map(str, wrong_positions))
        return f"Questions {position_list} are incorrect"


def first_wrong_index(code_attempt: str, correct_answers: List[str]) -> Optional[int]:
    """Returns 0-based index of first wrong position, or None if all correct or invalid"""
    if not code_attempt:
        return None
    code_upper = code_attempt.upper()
    if len(code_upper) < 1:
        return None
    for i in range(min(len(code_upper), 3)):
        if i < len(correct_answers) and code_upper[i] != correct_answers[i]:
            return i
    if len(code_upper) == 3 and "".join(correct_answers) == code_upper:
        return None
    return None


def show_welcome():
    """Display welcome screen"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/4335/4335164.png", width=150)

    st.markdown(f"## 👋 Welcome to {STATION_DATA['station_name']}")
    st.markdown("""
    Here we will play escape room quiz. The rules are simple:

    1. 📝 Answer all questions and write down your answers
    2. 🔑 Convert your answers into a **code** (e.g. ABC)
    3. ✅ Enter the code to proceed to the next station
    4. 💡 You can use help, but it comes with **time penalties**
    """)

    st.markdown("### 🔑 Enter access code to begin")
    st.markdown("Code format: <span class='code-format'>XY123</span> (2 letters + 3 digits)", unsafe_allow_html=True)


# ---------------------------
# Main
# ---------------------------

def main():
    station_data = STATION_DATA
    initialize_session()

    station_number = station_data["station_number"]
    station_name = station_data["station_name"]

    # Access gate
    if st.session_state.group_id is None:
        show_welcome()

        col1, col2 = st.columns([3, 1])
        with col1:
            access_code = st.text_input(
                "📝 Access code:",
                value=st.session_state.access_code,
                key="access_code_input",
                placeholder="Format: XY123 (e.g. AB123)"
            )

        with col2:
            start_btn = st.button("🚀 Start", use_container_width=True)

        if start_btn:
            st.session_state.access_code = access_code
            code_upper = access_code.strip().upper()

            access_code_match = None
            for stored_code, group in station_data["access_codes"].items():
                if stored_code.strip().upper() == code_upper:
                    access_code_match = stored_code
                    break

            if access_code_match:
                group_id = station_data["access_codes"][access_code_match]
                group_data = station_data["groups"][group_id]

                st.session_state.group_id = group_id
                st.session_state.group_name = group_data["name"]
                st.session_state.start_time = datetime.now()
                st.session_state.questions = group_data["questions"]
                st.session_state.next_station = group_data["next_station"]
                st.session_state.next_code = group_data["next_code"]
                st.session_state.is_final = group_data["is_final"]

                st.success(f"✅ Welcome, {group_data['name']}!")
                st.rerun()
            else:
                st.error("❌ Invalid access code!")
        return

    # Group data
    group_id = st.session_state.group_id
    group_data = station_data["groups"][group_id]
    group_name = group_data["name"]
    questions = st.session_state.questions
    next_station = st.session_state.next_station
    next_code = st.session_state.next_code
    is_final = st.session_state.is_final

    # Title
    st.title(f"🧬 {station_name}")
    st.subheader(f"👥 {group_name}")

    if st.session_state.total_penalties > 0:
        st.metric("⚠️ Total penalties", f"+{st.session_state.total_penalties}s")

    # Quiz body
    if not st.session_state.quiz_completed:
        st.markdown(f"### 📋 Questions")

        correct_answers = [q["correct"] for q in questions]
        correct_code = "".join(correct_answers)

        # Render questions (no radios)
        for i, q in enumerate(questions):
            st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
            st.markdown(f"#### 🔢 Question {i+1}")
            st.write(q["question"])
            for option in q["options"]:
                st.write(f"   {option}")
            st.markdown('</div>', unsafe_allow_html=True)

        # One-shot banners with TTL (30s)
        now = datetime.now()

        # Hint banner
        if st.session_state.hint_until and isinstance(st.session_state.hint_until, datetime):
            if now < st.session_state.hint_until:
                st.markdown('<div class="hint-box">', unsafe_allow_html=True)
                st.info(f"💡 Hint: {st.session_state.hint_text}")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.session_state.hint_until = None
                st.session_state.hint_text = ""

        # Answer banner
        if st.session_state.answer_until and isinstance(st.session_state.answer_until, datetime):
            if now < st.session_state.answer_until:
                st.markdown('<div class="answer-box">', unsafe_allow_html=True)
                st.success(f"🎯 Answer: {st.session_state.answer_text}")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.session_state.answer_until = None
                st.session_state.answer_text = ""

        # Check penalty status
        penalty_active = is_penalty_active()
        penalty_remaining = get_penalty_remaining()

        # Show penalty warning if active
        if penalty_active:
            st.markdown('<div class="penalty-warning">', unsafe_allow_html=True)
            st.warning(f"⚠️ Code verification blocked for {penalty_remaining} seconds due to penalty")
            st.markdown('</div>', unsafe_allow_html=True)

        # Verification
        st.markdown("### 🎯 Verification and moving to next station")

        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            # Reset input value when a new penalty starts
            input_value = ""
            if penalty_active:
                if st.session_state.penalty_triggered:
                    st.session_state.penalty_triggered = False
                    input_value = ""
                else:
                    input_value = st.session_state.last_code_attempt

                verification_code = st.text_input(
                    "🔑 Code:",
                    disabled=True,
                    value=input_value,
                    key="code_input",
                    help="🚫 Blocked due to penalty"
                )
            else:
                verification_code = st.text_input(
                    "🔑 Enter code:",
                    placeholder="Three letters (e.g. ABC)",
                    max_chars=3,
                    key="code_input"
                )

        with col2:
            if penalty_active:
                st.markdown(f'<div class="timer-display">⛔ {penalty_remaining}s</div>', unsafe_allow_html=True)
                progress = 1 - (penalty_remaining / 60) if penalty_remaining <= 60 else 0
                st.progress(max(0, progress))

        with col3:
            if penalty_active:
                st.button("✅ Verify code", disabled=True)
            else:
                if st.button("✅ Verify code", use_container_width=True):
                    st.session_state.last_code_attempt = verification_code

                    if verification_code.upper() == correct_code:
                        st.balloons()
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)

                        if is_final:
                            st.success("🎉 CONGRATULATIONS! You've completed all stations!")
                            st.markdown("### 🏆 Your completion code:")
                            st.markdown(f"<span class='code-format'>{next_code}</span>", unsafe_allow_html=True)
                            st.markdown("Please enter this code into the central computer.")
                        else:
                            st.success("🎉 SUCCESS! You're moving to the next station!")
                            st.markdown("### 🗺️ Continue to the next station:")
                            st.markdown(f"Next station: **{next_station}**")
                            st.markdown(f"Code for next station: <span class='code-format'>{next_code}</span>", unsafe_allow_html=True)

                        st.markdown('</div>', unsafe_allow_html=True)
                        st.session_state.quiz_completed = True
                        return
                    else:
                        st.error("❌ Incorrect code!")
                        add_penalty_cooldown(30)  # fixed 30s penalty for wrong code
                        st.warning("⚠️ +30s penalty!")

        # Help section - ALWAYS AVAILABLE
        st.markdown("### 🆘 Help")
        
        if penalty_active:
            st.info("ℹ️ Help functions are available even during penalty time")

        help_col1, help_col2 = st.columns(2)

        with help_col1:
            hint_button_text = f"💡 Show incorrect question (+30s)"
            if st.session_state.hint_count > 0:
                hint_button_text += f" [{st.session_state.hint_count}x]"

            # Help buttons are NEVER disabled
            if st.button(hint_button_text, use_container_width=True, key="hint_btn"):
                # Fixed +30s penalty, cumulative if active
                add_penalty_cooldown(30)
                st.session_state.hint_count += 1

                current_code_input = st.session_state.get('code_input', '')
                idx = first_wrong_index(current_code_input, correct_answers)
                if idx is None:
                    hint_text = "Enter code to analyze or answers are already correct"
                else:
                    hint_text = f"Question {idx + 1} is incorrect"

                st.session_state.hint_text = hint_text
                st.session_state.hint_until = datetime.now() + timedelta(seconds=30)  # show for 30s
                st.rerun()  # Immediate refresh to show the hint

        with help_col2:
            answer_button_text = f"🎯 Reveal correct answer (+60s)"
            if st.session_state.answer_count > 0:
                answer_button_text += f" [{st.session_state.answer_count}x]"

            # Help buttons are NEVER disabled
            if st.button(answer_button_text, use_container_width=True, key="answer_btn"):
                # Fixed +60s penalty, cumulative if active
                add_penalty_cooldown(60)
                st.session_state.answer_count += 1

                current_code_input = st.session_state.get('code_input', '')
                idx = first_wrong_index(current_code_input, correct_answers)
                if idx is None:
                    ans_text = "All answers are correct or no code to evaluate"
                else:
                    ans_text = f"Question {idx + 1}: Correct answer is {correct_answers[idx]}"

                st.session_state.answer_text = ans_text
                st.session_state.answer_until = datetime.now() + timedelta(seconds=30)  # banner visible 30s
                st.rerun()  # Immediate refresh to show the answer

    # Optimized auto-refresh - only refresh every 5 seconds during penalty, not every second
    if not st.session_state.quiz_completed and is_penalty_active():
        current_time = datetime.now()
        last_check = st.session_state.last_penalty_check
        
        # Only refresh every 5 seconds instead of every second
        if last_check is None or (current_time - last_check).total_seconds() >= 5:
            st.session_state.last_penalty_check = current_time
            time.sleep(5)
            st.rerun()


if __name__ == "__main__":
    main()
