from df_load_preprocess import anime_df
from similarity_func import cosine_sim, tfidf_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

def get_recommendations(df, cosine_sim_matrix):
    # Prompt the user to enter the title of the anime
    title = input("Enter the name of the anime: ")
    
    # Get the index of the anime that matches the title
    idx = df.index[df['name'] == title].tolist()[0]

    # Get the pairwise similarity scores of all animes with that anime
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # Sort the anime by similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar animes
    sim_scores = sim_scores[1:10]

    # Get the anime indices
    anime_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar animes
    return df['name'].iloc[anime_indices]

# Call the function and print the recommendations
recommended_animes = get_recommendations(anime_df, cosine_sim)
print(recommended_animes)
