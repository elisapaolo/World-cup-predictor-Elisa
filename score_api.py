import streamlit as st
import requests

def fetch_latest_scores():
    api_key = st.secrets.get("API_FOOTBALL_KEY", None)

    if not api_key:
        st.warning("API_FOOTBALL_KEY not configured.")
        return None

    headers = {"x-apisports-key": api_key}
    url = "https://v3.football.api-sports.io/fixtures?league=1&season=2026"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    st.error(f"API Error: {response.status_code}")
    return None
