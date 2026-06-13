# World Cup Predictor — Version 2

This Streamlit app lets you update World Cup scores, recalculate group standings, and simulate advancement odds.

## What is new in Version 2

- Manual score entry still works.
- A new **Fetch latest scores from API** button can pull scores from API-Football.
- If no API key is configured, the app still runs and explains what is missing.

## Run locally

```bash
cd worldcup_predictor_app
pip install -r requirements.txt
streamlit run app.py
```

## Enable automatic score updates

1. Create an API-Football/API-Sports account.
2. Get your API key.
3. For local use, create this file:

```bash
mkdir -p .streamlit
cp .streamlit_secrets_example.toml .streamlit/secrets.toml
```

4. Edit `.streamlit/secrets.toml` and paste your key:

```toml
API_FOOTBALL_KEY = "your_real_key_here"
```

5. Restart Streamlit and click **Fetch latest scores from API**.

## Deploy to Streamlit Cloud

1. Upload this folder to GitHub.
2. Create a Streamlit Cloud app pointing to `app.py`.
3. In Streamlit Cloud, go to **Settings > Secrets** and add:

```toml
API_FOOTBALL_KEY = "your_real_key_here"
```

4. Reboot the app.

## Notes

API-Football identifies the FIFA World Cup with `league=1` and `season=2026`. The app uses those defaults. The starter match file includes group-stage matches and the model uses starter Elo ratings that you can tune later.
