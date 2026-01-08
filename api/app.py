from flask import Flask, jsonify
import joblib
from scipy.sparse import load_npz

song_metadata = joblib.load(f"{MODEL_DIR}/song_metadata.pkl")

# Model artifacts
MODEL_DIR = "../model"

als_model = joblib.load(f"{MODEL_DIR}/als_model.pkl")
user_item_matrix = load_npz(f"{MODEL_DIR}/user_item_matrix.npz")
user_id_mapping = joblib.load(f"{MODEL_DIR}/user_id_mapping.pkl")
id_to_song = joblib.load(f"{MODEL_DIR}/id_to_song.pkl")

# function for recommending songs
def recommend_songs(original_user_id, N=10):
    if original_user_id not in user_id_mapping:
        return []

    internal_user_id = user_id_mapping[original_user_id]
    user_items = user_item_matrix[internal_user_id]

    item_ids, scores = als_model.recommend(
        userid=internal_user_id,
        user_items=user_items,
        N=N
    )

    recommendations = []

    for internal_item_id in item_ids:
        song_id = id_to_song.get(internal_item_id)

        if song_id is None:
            continue

        meta = song_metadata.get(song_id, {})

        recommendations.append({
            "song_id": song_id,
            "artist_name": meta.get("artist_name"),
            "genre_ids": meta.get("genre_ids"),
            "language": meta.get("language")
        })

    return recommendations

# flask
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "Music Recommendation API is running"
    })

@app.route("/users")
def get_sample_users():
    return jsonify({
        "sample_users": list(user_id_mapping.keys())[:10]
    })

@app.route("/recommend/<string:msno>")
def recommend(msno):
    songs = recommend_songs(msno, N=10)

    if not songs:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "user": msno,
        "recommendations": songs
    })


if __name__ == "__main__":
    app.run(debug=True)
