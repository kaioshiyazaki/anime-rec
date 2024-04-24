import sqlite3
import pandas as pd 

# Load the data from the SQLite database
def load():
    conn = sqlite3.connect('anime.db')
    query = "SELECT * FROM anime_data"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

anime_df = load()

# Print DataFrame columns to verify 'genres' column existence
print("DataFrame Columns:", anime_df.columns.tolist())

# Preprocess the data: if values are missing in 'genre', we drop the row
def preprocess_data(df):
    # Check if 'genres' column exists
    if 'genre' in df.columns:
        df = df.dropna(subset=['genre'])
    else:
        print("Error: 'genre' column does not exist in the DataFrame.")
    return df

anime_df = preprocess_data(anime_df)


