import streamlit as st
import pandas as pd
from score_api import fetch_latest_scores

st.set_page_config(page_title="World Cup Predictor", layout="wide")

st.title("World Cup Predictor")
st.write("View 2026 World Cup matches, scores, and prediction data.")

if st.button("Fetch latest World Cup data"):
    data = fetch_latest_scores()

    if data and "response" in data:
        fixtures = []

        for item in data["response"]:
            fixture = item["fixture"]
            teams = item["teams"]
            goals = item["goals"]

            fixtures.append({
                "Date": fixture["date"],
                "Venue": fixture["venue"]["name"] if fixture.get("venue") else "",
                "City": fixture["venue"]["city"] if fixture.get("venue") else "",
                "Home Team": teams["home"]["name"],
                "Away Team": teams["away"]["name"],
                "Home Goals": goals["home"],
                "Away Goals": goals["away"],
                "Status": fixture["status"]["long"]
            })

        df = pd.DataFrame(fixtures)

        st.success("API connected successfully.")
        st.subheader("2026 World Cup Fixtures")
        st.dataframe(df, use_container_width=True)

    else:
        st.warning("No data returned. Check your API key or plan.")

else:
    st.info("Click the button above to fetch the latest World Cup data.")
