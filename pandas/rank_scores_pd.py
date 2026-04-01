import pandas as pd

def rank_scores(data):

    df = pd.DataFrame(data)

    # Apply dense rank
    df['rank'] = df['score'].rank(method='dense', ascending=False)

    # Select required columns and sort
    result = df[['score', 'rank']].sort_values(by='score', ascending=False)

    return result

dt = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}

print(rank_scores(dt))