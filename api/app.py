from flask import Flask, jsonify
import joblib
from scipy.sparse import load_npz

# Model artifacts

MODEL_DIR = "../model"

als_model = joblib.load(f"{MODEL_DIR}/als_model.pkl")
user_item_matrix = load_npz(f"{MODEL_DIR}/user_item_matrix.npz")
user_id_mapping = joblib.load(f"{MODEL_DIR}/user_id_mapping.pkl")
id_to_song = joblib.load(f"{MODEL_DIR}/id_to_song.pkl")