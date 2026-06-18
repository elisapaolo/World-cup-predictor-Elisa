import streamlit as st
import pandas as pd
from score_api import fetch_latest_scores
from predictor import predict_match
from tournament import simulate_full_tournament

st.set_page_config(page_title="World Cup Predictor", layout="wide")

st.title("World Cup Predictor")
st.write("2026 World Cup fixtures, scores, stages, and predictions.")

if st.button("Fetch latest World Cup data"):
    data = fetch_latest_scores()

    if data and "response" in data:
        fixtures = []

        for item in data["response"]:
            fixture = item["fixture"]
            teams = item["teams"]
            goals = item["goals"]
            league = item["league"]

            prediction = predict_match(
    teams["home"]["name"],
    teams["away"]["name"]
)

            fixtures.append({
                "Stage": league.get("round", ""),
                "Date": fixture["date"],
                "Venue": fixture["venue"]["name"] if fixture.get("venue") else "",
                "City": fixture["venue"]["city"] if fixture.get("venue") else "",
                "Home Team": teams["home"]["name"],
                "Away Team": teams["away"]["name"],
                "Home Goals": goals["home"],
                "Away Goals": goals["away"],
                "Status": fixture["status"]["long"],
               "Pred Home Goals": prediction["pred_score1"],
"Pred Away Goals": prediction["pred_score2"],
"Home Win %": prediction["team1_win_pct"],
"Draw %": prediction["draw_pct"],
"Away Win %": prediction["team2_win_pct"],
            })

        df = pd.DataFrame(fixtures)
        tournament_results = simulate_full_tournament(df)

        st.success(f"API connected successfully. {len(df)} matches loaded.")

group_tab, r32_tab, r16_tab, qf_tab, sf_tab, final_tab, prediction_tab = st.tabs([
    "Group Stage",
    "Round of 32",
    "Round of 16",
    "Quarterfinals",
    "Semifinals",
    "Final",
    "Tournament Prediction"
])

    with group_tab:
            group_df = df[df["Stage"].str.contains("Group", case=False, na=False)]
            st.subheader("Group Stage Matches")
            st.dataframe(group_df, use_container_width=True)

    with r32_tab:
            r32_df = df[df["Stage"].str.contains("Round of 32", case=False, na=False)]
            st.subheader("Round of 32")
            st.dataframe(r32_df, use_container_width=True)

    with r16_tab:
            r16_df = df[df["Stage"].str.contains("Round of 16", case=False, na=False)]
            st.subheader("Round of 16")
            st.dataframe(r16_df, use_container_width=True)

    with qf_tab:
            qf_df = df[df["Stage"].str.contains("Quarter", case=False, na=False)]
            st.subheader("Quarterfinals")
            st.dataframe(qf_df, use_container_width=True)

    with sf_tab:
            sf_df = df[df["Stage"].str.contains("Semi", case=False, na=False)]
            st.subheader("Semifinals")
            st.dataframe(sf_df, use_container_width=True)

    with final_tab:
            final_df = df[df["Stage"].str.contains("Final", case=False, na=False)]
            st.subheader("Final")
            st.dataframe(final_df, use_container_width=True)
            
    with prediction_tab:
            st.subheader("Predicted Tournament Results")
            st.write(tournament_results)

    else:
        st.warning("No data returned. Check your API key or plan.")

else:
    st.info("Click the button above to fetch the latest World Cup data.")
