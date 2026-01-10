# 🎵 RhythmAI - Music Recommendation System

**RhythmAI** is an end-to-end **Music Recommendation System** built using the **KKBOX dataset**.  
It leverages **implicit-feedback collaborative filtering** with **Alternating Least Squares (ALS)** to generate **personalized music recommendations**, delivered through a **Flask REST API** and an **interactive web-based UI**.

The project follows a **real-world recommender system pipeline**, supporting **offline model training** and **online inference with live user interaction**.

---

## 🚀 Features

* Personalized music recommendations per user
* Collaborative Filtering using implicit feedback
* Matrix Factorization with ALS (Implicit library)
* Model persistence using Joblib
* REST API for real-time recommendations
* Metadata enrichment (artist, genre, language)
* Interactive frontend UI (HTML, CSS, JavaScript)
* Clean separation of training, serving, and UI layers
* Easily extensible for future improvements

---

## 🖥️ User Interface Preview

Below is the web-based UI for RhythmAI, where users can enter a user ID (`msno`) and instantly receive personalized music recommendations.

![RhythmAI UI Screenshot](ui_screenshots/ui_demo.png)

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
Frontend UI (HTML + CSS + JS)
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
| Backend API     | Flask                  |
| Frontend        | HTML, CSS, JavaScript  |
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
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
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

### 🔹 Web UI

```
GET /ui
```

* Enter a user ID (msno)
* Click Recommend
* View personalized recommendations instantly

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

Access the app:
🔹 API → http://127.0.0.1:5000/recommend/<msno>
🔹 UI → http://127.0.0.1:5000/ui

---

## 🔮 Future Improvements

* Cold-start handling for new users/songs
* Recommendation confidence scores
* Docker deployment
* Hybrid (content + collaborative) approach

---

## 🧑‍💻 Author

Aditi Sonkar

🔗 LinkedIn: https://www.linkedin.com/in/aditisonkar12/

---

## 🏷️ License

This project is licensed under the MIT License — free to use, modify, and distribute.

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](...)

---

## ⭐ If you like this project, don’t forget to star the repo on GitHub!


