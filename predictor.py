def predict_match(team1, team2):

    ratings = {
        "Argentina": 95,
        "Spain": 92,
        "France": 94,
        "Brazil": 93,
        "England": 91,
        "Portugal": 89,
        "Germany": 88,
        "Netherlands": 87,
        "Belgium": 86,
        "Uruguay": 84,
        "Croatia": 83,
        "Morocco": 82
    }

    team1_rating = ratings.get(team1, 70)
    team2_rating = ratings.get(team2, 70)

    total = team1_rating + team2_rating

    team1_win_pct = round(team1_rating / total * 100, 1)
    team2_win_pct = round(team2_rating / total * 100, 1)

    draw_pct = 100 - team1_win_pct - team2_win_pct

    if team1_rating > team2_rating:
        pred_score1 = 2
        pred_score2 = 1
    elif team2_rating > team1_rating:
        pred_score1 = 1
        pred_score2 = 2
    else:
        pred_score1 = 1
        pred_score2 = 1

    return {
        "pred_score1": pred_score1,
        "pred_score2": pred_score2,
        "team1_win_pct": team1_win_pct,
        "draw_pct": draw_pct,
        "team2_win_pct": team2_win_pct
    }
