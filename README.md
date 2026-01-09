# 🎵 RhythmAI - Music Recommendation System

**RhythmAI** is an end-to-end **Music Recommendation System** built using the **KKBOX dataset**.
It leverages **implicit-feedback collaborative filtering** with **Alternating Least Squares (ALS)** to generate **personalized song recommendations**, exposed via a **Flask REST API**.

The system supports **offline model training** and **online inference**, making it suitable for real-world recommender system pipelines.

---

## 🚀 Features

* Personalized music recommendations per user
* Collaborative Filtering using implicit feedback
* Matrix Factorization with ALS (Implicit library)
* Model persistence using Joblib
* REST API for real-time recommendations
* Metadata enrichment (artist, genre, language)
* Clean separation of training and serving
* Easily extensible for future improvements

---

## 🏗️ System Architecture

```
KKBOX Dataset
   ↓
Data Cleaning & EDA
   ↓
User–Item Interaction Matrix (Sparse)
   ↓
ALS Model Training (Implicit CF)
   ↓
Top-N Recommendation Generation
   ↓
Model Serialization (Joblib)
   ↓
Flask REST API
   ↓
JSON Recommendations with Metadata
```

---

## 🧩 Tech Stack

| Layer           | Technology             |
| --------------- | ---------------------- |
| Language        | Python                 |
| Data Processing | Pandas, NumPy          |
| Visualization   | Matplotlib             |
| ML Algorithm    | ALS (Implicit Library) |
| Sparse Ops      | SciPy                  |
| Model Storage   | Joblib                 |
| API             | Flask                  |
| Version Control | Git & GitHub           |

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-lightblue)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Storage-yellow)
![API](https://img.shields.io/badge/API-Flask%20%2F%20FastAPI-red)

---

## 📁 Project Structure

```
music-recommendation-system/
│
├── api/
│   └── app.py
│
├── data/
│   └── songs.csv
│
├── model/
│   ├── als_model.pkl
│   ├── user_item_matrix.npz
│   ├── user_id_mapping.pkl
│   ├── id_to_song.pkl
│   └── song_metadata.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model_als.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Recommendation Approach

* **Algorithm**: Alternating Least Squares (ALS)
* **Feedback Type**: Implicit (listening behavior)
* **Why ALS?**

  * Scales well with sparse user–item matrices
  * Widely used in industry recommender systems
  * Efficient for large datasets

---

## 🌐 API Endpoints

### 🔹 Health Check

```
GET /
```

**Response**

```json
{
  "status": "Music Recommendation API is running"
}
```

---

### 🔹 Get Sample Users

```
GET /users
```

**Response**

```json
{
  "sample_users": ["++5wYj0MgQHoRuD3GbbvmphZbBBwymzv5Q4l8sywtuU=", "..."]
}
```

---

### 🔹 Get Recommendations

```
GET /recommend/<msno>
```

**Example Response**

```json
{
  "user": "++5wYj0MgQHoRuD3GbbvmphZbBBwymzv5Q4l8sywtuU=",
  "recommendations": [
    {
      "song_id": "ZmekVY4j...",
      "artist": "David Bowie",
      "genres": ["Pop"],
      "language": "English"
    }
  ]
}
```

---

## 🧑‍💻 Author

Aditi Sonkar

🔗 LinkedIn: https://www.linkedin.com/in/aditisonkar12/

---

## 🏷️ License

This project is licensed under the MIT License — free to use, modify, and distribute.

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](...)

---

## 🚧 Work in Progress

---

## ⭐ If you like this project, don’t forget to star the repo on GitHub!










# 🎵 RhythmAI – Music Recommendation System



---

## 🚀 Key Features



---

## 🏗️ System Architecture


---





## 🧩 Tech Stack



---

## 📁 Project Structure



---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/music-recommendation-system.git
cd music-recommendation-system
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd api
python app.py
```

Visit:
👉 `http://127.0.0.1:5000/recommend/<msno>`

---

## 🔮 Future Improvements

* Cold-start handling for new users/songs
* Popularity bias correction
* Recommendation confidence scores
* Hybrid (content + collaborative) approach
* Frontend UI for recommendations
* Docker deployment

---

## 🧑‍💻 Author

**Aditi Sonkar**

🔗 LinkedIn: [https://www.linkedin.com/in/aditisonkar12/](https://www.linkedin.com/in/aditisonkar12/)
🔗 GitHub: [https://github.com/aditisonkar12](https://github.com/aditisonkar12)

---

## 🏷️ License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ⭐ If you like this project, don’t forget to star the repo!
