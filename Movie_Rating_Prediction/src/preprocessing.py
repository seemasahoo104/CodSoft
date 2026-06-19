import pandas as pd

def load_data():

    df = pd.read_csv(
        "data/IMDb Movies India.csv",
        encoding='latin1'
    )

    # Remove rows with missing ratings
    df = df.dropna(subset=['Rating'])

    # Fill missing values
    columns = ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']

    for col in columns:
        df[col] = df[col].fillna('Unknown')

    # Combine features
    df['Features'] = (
        df['Genre'] + " " +
        df['Director'] + " " +
        df['Actor 1'] + " " +
        df['Actor 2'] + " " +
        df['Actor 3']
    )

    return df