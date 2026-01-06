# Movie Recommendation System using Collaborative Filtering

## Project Overview

This project is an AI-powered movie recommendation system that suggests movies to users based on their previous ratings and preferences. The system uses collaborative filtering, which means it recommends movies by finding users with similar tastes and suggesting movies they liked.

The goal of this project is to understand how recommendation systems work in real-world applications like Netflix or Amazon Prime and to implement a basic version using Python and machine learning concepts.

## Technologies Used

- Python

- Pandas

- Scikit-learn

- Flask

- NumPy

## Dataset
The dataset used for this project is taken from Kaggle (Movie Recommendation System).
It contains two main files:

- ratings.csv – user ratings for movies
https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system?select=ratings.csv

- movies.csv – movie titles and genres
https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system?select=movies.csv

## Project Structure
```
movie_recommender/
│
├── app.py                # Flask API
├── recommender.py        # Recommendation logic
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignored files and folders
└── data/                 # Dataset folder (not tracked by Git)
```
## Methodology

1 . Load user ratings and movie metadata

2 . Construct a user–movie rating matrix

3 . Apply cosine similarity to measure similarity between users

4 . Identify users with similar rating behavior

5 . Recommend movies highly rated by similar users

6 . Return the Top 10 recommended movies for a given user

## Running the Project

#### Install Dependencies
```
pip install -r requirements.txt
```

#### Start the Flask Server
```
python app.py
```

#### The server will start at:
```
http://127.0.0.1:5000
```
### Get Recommendations

Use the following endpoint in the browser:
```
http://127.0.0.1:5000/recommend/<user_id>
```
Example:
```
http://127.0.0.1:5000/recommend/7045
```
### Sample Output (JSON)
```
[
  {
    "movieId": 1,
    "title": "Toy Story (1995)",
    "genres": "Adventure|Animation|Children|Comedy|Fantasy"
  },
  {
    "movieId": 2,
    "title": "Jumanji (1995)",
    "genres": "Adventure|Children|Fantasy"
  }
]
```
## Features

- Personalized movie recommendations

- User-based collaborative filtering

- Flask-based REST API

- Clean and modular code structure

- Handles large datasets using sampling
