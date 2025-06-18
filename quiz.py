# streamlit_quiz.py

import streamlit as st
import json
import random
from utils.data import load_json_file, save_json_file
from ui.welcome import show_welcome


QUESTIONS_FILE = "questions/questions_db.json"
SCORES_FILE = "questions/scores.json"

def load_questions():
    all_questions = load_json_file(QUESTIONS_FILE)
    mc_questions = [q for q in all_questions if q.get("type") != "order"]
    order_questions = [q for q in all_questions if q.get("type") == "order"]

    if len(mc_questions) < 18 or len(order_questions) < 2:
        st.error("Not enough questions in the database.")
        st.stop()

    selected_mc = random.sample(mc_questions, 18)
    selected_order = random.sample(order_questions, 2)

    return random.sample(selected_mc + selected_order, 20)

def init_state():
    if "index" not in st.session_state:
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.questions = load_questions()
        st.session_state.answered = False
        st.session_state.feedback = ""

def run_quiz():
    if "started" not in st.session_state or not st.session_state.started:
        show_welcome()
        return

    st.title("🧠 SPM Quiz")
    init_state()

    if st.session_state.index >= len(st.session_state.questions):
        percent = (st.session_state.score / len(st.session_state.questions)) * 100
        st.success(f"Quiz complete! Your score: {percent:.1f}%")

        name = st.text_input("Enter your name to save your score:", value="Anonymous")
        if st.button("💾 Save Score"):
            data = load_json_file(SCORES_FILE)
            data.append({"name": name, "score": percent})
            save_json_file(SCORES_FILE, data)
            best = max(d["score"] for d in data)
            st.info(f"Best score so far: {best:.1f}%")
        return

    q = st.session_state.questions[st.session_state.index]
    st.subheader(f"Q{st.session_state.index + 1}: {q['question']}")

    if q.get("type") == "order":
        items = st.session_state.get("current_items")
        if not items:
            items = random.sample(q["choices"]["items"], len(q["choices"]["items"]))
            st.session_state.current_items = items

        reordered = st.multiselect("Reorder the steps:", items, default=items, key="user_order")

        if st.button("✅ Submit") and not st.session_state.answered:
            if reordered == q["correct_order"]:
                st.session_state.feedback = "✅ Correct order!"
                st.session_state.score += 1
            else:
                st.session_state.feedback = f"❌ Incorrect order.\nExpected: {q['correct_order']}"
            st.session_state.answered = True

    else:
        options = []
        for k in ['a', 'b', 'c', 'd', 'e']:
            text = q["choices"].get(k)
            if text:
                options.append((k, text))

        selected = st.multiselect("Choose the correct answers:", [f"{k}) {text}" for k, text in options], key="mc_answers")

        if st.button("✅ Submit") and not st.session_state.answered:
            selected_keys = {opt.split(")")[0] for opt in selected}
            correct = set(q["correct_answers"])

            if selected_keys == correct:
                st.session_state.feedback = "✅ Correct!"
                st.session_state.score += 1
            else:
                st.session_state.feedback = f"❌ Incorrect.\nExplanation: {q.get('explanation', 'No explanation.')}"
            st.session_state.answered = True

    if st.session_state.answered:
        st.markdown(st.session_state.feedback)
        if st.button("➡️ Next Question"):
            st.session_state.index += 1
            st.session_state.answered = False
            if "current_items" in st.session_state:
                del st.session_state.current_items
            st.rerun()


run_quiz()
