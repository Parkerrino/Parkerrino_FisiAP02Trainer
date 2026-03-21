import streamlit as st
import json
import random
import os

# Load questions
@st.cache_data
def load_questions():
    try:
        with open('questions.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        if 'AP02_Pruefung_Block1' not in data:
            st.error("❌ questions.json fehlt 'AP02_Pruefung_Block1'. Fix JSON!")
            st.stop()
        return data['AP02_Pruefung_Block1']
    except Exception as e:
        st.error(f"❌ JSON laden fehlgeschlagen: {e}")
        st.stop()
        return {}

# App
st.set_page_config(page_title="AP02 Fisi Trainer", page_icon="🚀", layout="wide")

st.info("👉 **App starten:** `streamlit run app.py` (nicht `python app.py`)")

st.title("🚀 Moderner AP02 Fisi Trainer")
st.markdown("**Zufällige Fragen aus AP02 Prüfungsblock 1.** Erweitere `questions.json`!")

if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.questions = load_questions()
    st.session_state.current_question = None
    st.session_state.field_name = None

# Sidebar
st.sidebar.header("Einstellungen")
st.sidebar.success("📚 AP02 Prüfungsblock 1")

if st.sidebar.button("Neue Session starten", type="primary"):
    st.session_state.score = 0
    st.session_state.total = 0
    st.rerun()

# questions is now the list directly
questions_list = st.session_state.questions

# Generate question
if st.session_state.current_question is None:
    field_questions = questions_list  # Single field list
    st.session_state.current_question = random.choice(field_questions)
    st.session_state.field_name = "AP02 Block 1"

with st.container():
    col1, col2 = st.columns([3, 1])
    with col2:
        st.metric("Score", f"{st.session_state.score}/{st.session_state.total}", delta=f"{st.session_state.score/st.session_state.total*100:.0f}%" if st.session_state.total > 0 else "0%")

    st.markdown(f"**{st.session_state.field_name}:**")
    st.markdown(f"### {st.session_state.current_question['question']}")

    options = st.session_state.current_question['options']
    selected = st.radio("Antwort:", options, key="question_radio", index=None)

    col_next, col_show = st.columns(2)
    if col_next.button("Antwort prüfen"):
        if selected:
            correct_idx = st.session_state.current_question['correct']
            is_correct = options.index(selected) == correct_idx
            st.session_state.total += 1
            if is_correct:
                st.session_state.score += 1
                st.success("✅ Richtig!")
            else:
                st.error(f"❌ Falsch! Korrekte Antwort: **{options[correct_idx]}**")
            
            st.rerun()
        else:
            st.warning("Wähle eine Antwort!")

    if col_show.button("Lösung anzeigen"):
        correct_idx = st.session_state.current_question['correct']
        st.info(f"**Korrekte Antwort:** {options[correct_idx]}")

    if st.button("Nächste Frage"):
        st.session_state.current_question = None
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("**Erweiterung:** Füge Fragen in `questions.json` hinzu. Format: `{\"question\": \"...\", \"options\": [\"A\", \"B\"], \"correct\": 1}`")
st.text("Hallo Charlie :)")