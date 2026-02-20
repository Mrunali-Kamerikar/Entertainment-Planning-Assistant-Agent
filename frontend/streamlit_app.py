# frontend/streamlit_app.py

import streamlit as st
import sys
import os

# Allow importing from app/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.agent_router import EntertainmentAgent


st.set_page_config(
    page_title="🎬 AI Entertainment Assistant",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "agent" not in st.session_state:
    st.session_state.agent = EntertainmentAgent()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------- LOGIN PAGE ----------
if not st.session_state.logged_in:

    st.title("🎬 Entertainment Planning Assistant")
    st.subheader("Login to continue")

    username = st.text_input("Enter Username")

    if st.button("Login"):
        if username.strip() != "":
            st.session_state.agent.login(username)
            st.session_state.logged_in = True
            st.success(f"Welcome, {username}!")
            st.rerun()

    st.stop()


# ---------- MAIN DASHBOARD ----------
st.title("🎥 Personalized AI Movie Assistant")

col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_input(
        "Ask for recommendations, summary, review, or Q&A",
        placeholder="e.g., recommend a sad movie"
    )

with col2:
    rating_movie = st.text_input("Rate a movie (Title)")
    rating_value = st.slider("Rating", 1, 5, 3)

    if st.button("Submit Rating"):
        if rating_movie:
            response = st.session_state.agent.handle_query(
                f"rate {rating_movie} {rating_value}"
            )
            st.success(response["response"])


# ---------- HANDLE QUERY ----------
if query:

    result = st.session_state.agent.handle_query(query)

    st.markdown("---")
    st.subheader("📌 Intent Detected:")
    st.info(result["intent"].capitalize())

    st.markdown("---")
    st.subheader("🎬 AI Response")

    st.write(result["response"])

    st.markdown("---")


# ---------- SIDEBAR ----------
st.sidebar.title("📊 User Controls")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧠 Features Enabled")
st.sidebar.markdown("""
- Personalized Ranking
- Genre Learning
- Rating Boost
- History Penalty
- Multi-user Memory
- Explainable AI Scoring
""")
