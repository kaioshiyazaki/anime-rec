from df_load_preprocess import anime_df
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def feature_engineering(df):
    # Instantiate the vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    # Fit and transform the 'genres' column
    tfidf_matrix = tfidf.fit_transform(df['genre'])
    return tfidf_matrix

tfidf_matrix = feature_engineering(anime_df)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
