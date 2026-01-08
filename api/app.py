from flask import Flask, jsonify
import joblib
from scipy.sparse import load_npz

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

    return [id_to_song[i] for i in item_ids]
