# streamlit_drag_order.py

import streamlit as st
import json
import random

QUESTIONS_FILE = "questions/questions_db.json"

def load_order_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        all_qs = json.load(f)
    return [q for q in all_qs if q.get("type") == "order"]

def init_state(order_questions):
    if "index" not in st.session_state:
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.order_questions = random.sample(order_questions, len(order_questions))
        st.session_state.feedback = ""
        st.session_state.submitted = False

    if "current_items" not in st.session_state:
        current_q = st.session_state.order_questions[st.session_state.index]
        st.session_state.current_items = random.sample(current_q["choices"]["items"], len(current_q["choices"]["items"]))

def run_drag_order_quiz():
    st.title("🔀 Order the Process Steps")

    order_questions = load_order_questions()
    init_state(order_questions)

    if st.session_state.index >= len(st.session_state.order_questions):
        st.success(f"Quiz complete! You scored {st.session_state.score}/{len(order_questions)}.")
        if st.button("Restart"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
        return

    q = st.session_state.order_questions[st.session_state.index]
    st.subheader(f"Q{st.session_state.index+1}: {q['question']}")

    reordered = st.multiselect(
        "🧩 Arrange in the correct order",
        options=st.session_state.current_items,
        default=st.session_state.current_items,
        key="user_order"
    )

    if st.button("✅ Submit"):
        correct_order = q["correct_order"]
        if reordered == correct_order:
            st.session_state.feedback = "✅ Correct!"
            st.session_state.score += 1
        else:
            st.session_state.feedback = f"❌ Incorrect order.\n\nExpected: {correct_order}"
        st.session_state.submitted = True

    if st.session_state.submitted:
        st.markdown(st.session_state.feedback)

        if st.button("➡️ Next Question"):
            st.session_state.index += 1
            del st.session_state["current_items"]
            st.session_state.submitted = False
            st.rerun()
