import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# LIMIT DATA SIZE (CRITICAL)
ratings = pd.read_csv("data/ratings.csv").head(5000)
movies = pd.read_csv("data/movies.csv")

# Keep only movies that appear in ratings
movies = movies[movies["movieId"].isin(ratings["movieId"])]

# Create user-movie matrix safely
user_movie_matrix = ratings.pivot_table(
    index="userId",
    columns="movieId",
    values="rating",
    fill_value=0
)

# Compute similarity
user_similarity = cosine_similarity(user_movie_matrix)
def recommend_movies(user_id, top_n=10):
    if user_id not in user_movie_matrix.index:
        return movies.head(top_n)

    user_index = user_movie_matrix.index.get_loc(user_id)
    similar_users = user_similarity[user_index].argsort()[::-1][1:]

    recommended = set()

    for sim_user in similar_users:
        sim_ratings = user_movie_matrix.iloc[sim_user]
        liked = sim_ratings[sim_ratings >= 4].index

        for movie_id in liked:
            if user_movie_matrix.loc[user_id, movie_id] == 0:
                recommended.add(movie_id)

        if len(recommended) >= top_n:
            break

    return movies[movies["movieId"].isin(list(recommended))].head(top_n)
