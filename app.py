from flask import Flask, jsonify
from recommender import recommend_movies

app = Flask(__name__)

@app.route("/recommend/<int:user_id>")
def recommend(user_id):
    recommendations = recommend_movies(user_id)
    return jsonify(recommendations.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
