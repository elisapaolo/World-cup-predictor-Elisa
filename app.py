import streamlit as st
import pandas as pd
from score_api import fetch_latest_scores

st.set_page_config(page_title="World Cup Predictor", layout="wide")

st.title("World Cup Predictor")
st.write("Update scores, view group standings, and fetch latest results.")

@st.cache_data
def load_matches():
    return pd.read_csv("matches.csv")

matches = load_matches()

st.subheader("Matches")
edited_matches = st.data_editor(matches, num_rows="dynamic", use_container_width=True)

if st.button("Fetch latest scores from API"):
    data = fetch_latest_scores()
    if data:
        st.success("API connected successfully.")
        st.json(data)
    else:
        st.warning("No scores returned. Check your API key in Streamlit Secrets.")

st.subheader("Current Data")
st.dataframe(edited_matches, use_container_width=True)
