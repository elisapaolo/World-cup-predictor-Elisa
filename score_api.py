import streamlit as st
import requests

def fetch_latest_scores():
    api_key = st.secrets.get("API_FOOTBALL_KEY", None)

    if not api_key:
        st.warning("API_FOOTBALL_KEY not configured.")
        return None

    headers = {
        "x-apisports-key": api_key
    }

    url = "https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fv3.football.api-sports.io%2Ffixtures%3Fleague%3D1%26season%3D2026&data=05%7C02%7Celisa.paolo%40sap.com%7Ca7e81b920a774fd6966708dec96ee792%7C42f7676cf455423c82f6dc2d99791af7%7C0%7C0%7C639169675359413419%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=twxcBDoae4KTq%2F6%2Bu9ElypxxaLiHPZ1roM7Rauvoey4%3D&reserved=0"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    st.error(f"API Error: {response.status_code}")
    return None
API-Football identifies the FIFA World Cup with `league=1` and `season=2026`. The app uses those defaults. The starter match file includes group-stage matches and the model uses starter Elo ratings that you can tune later.
