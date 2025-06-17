# welcome.py (Streamlit-compatible)

import streamlit as st
import json
from utils.data import load_json_file

SCORES_FILE = "questions/scores.json"

def show_welcome():
    st.markdown("## 👋 Welcome to the SPM Quiz!")
    st.markdown("### 🏆 Top 5 Scores:")

    try:
        scores = load_json_file(SCORES_FILE)
    except:
        scores = []

    scores.sort(key=lambda x: x["score"], reverse=True)
    if scores:
        for i, s in enumerate(scores[:5]):
            st.markdown(f"{i+1}. **{s['name']}** — {s['score']:.1f}%")
    else:
        st.info("No scores yet.")

    name = st.text_input("Enter your name:", value="Anonymous")

    if st.button("🚀 Start Quiz"):
        st.session_state.username = name
        st.session_state.started = True
        st.rerun()
