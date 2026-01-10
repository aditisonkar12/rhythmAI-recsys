from flask import Flask, jsonify, send_from_directory, render_template
import joblib
from scipy.sparse import load_npz
import os
import math

# Model artifacts
MODEL_DIR = os.path.join(os.path.dirname(__file__), "../model")

als_model = joblib.load(f"{MODEL_DIR}/als_model.pkl")
user_item_matrix = load_npz(f"{MODEL_DIR}/user_item_matrix.npz")
user_id_mapping = joblib.load(f"{MODEL_DIR}/user_id_mapping.pkl")
id_to_song = joblib.load(f"{MODEL_DIR}/id_to_song.pkl")
song_metadata = joblib.load(f"{MODEL_DIR}/song_metadata.pkl")

# Genre mapping (extend later if needed)
GENRE_MAP = {
    "465": "Pop",
    "958": "Classical",
    "451": "Soundtrack",
    "2022": "Rock",
    "1259": "Indie",
    "458": "Mandarin Pop",
    "139": "Jazz"
}

# Language mapping
LANGUAGE_MAP = {
    3.0: "Mandarin",
    52.0: "English",
    -1.0: "Unknown"
}

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

        genre_raw = meta.get("genre_ids")
        genres = []
        if genre_raw is not None and not (isinstance(genre_raw, float) and math.isnan(genre_raw)):
            genre_str = str(int(genre_raw)) if isinstance(genre_raw, float) else str(genre_raw)

            for g in genre_str.split("|"):
                if g in GENRE_MAP:
                    genres.append(GENRE_MAP[g])



        recommendations.append({
            "song_id": song_id,
            "artist": meta.get("artist_name", "Unknown"),
            "genres": genres,
            "language": LANGUAGE_MAP.get(meta.get("language"), "Unknown")
        })

    return recommendations

# flask
app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

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

@app.route("/ui")
def serve_ui():
    frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
    return send_from_directory(frontend_path, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
