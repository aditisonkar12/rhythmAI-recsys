# 🎵 RhythmAI - Music Recommendation System

This project implements a **Music Recommendation System** using the **KKBOX dataset**.  
It analyzes user listening behavior and song information to generate **personalized music recommendations**.  
The trained machine learning model is exposed through a **REST API**, enabling real-time song recommendations.

---

## 🚀 Features

- Personalized song recommendations
- Implicit-feedback collaborative filtering
- Matrix Factorization using ALS
- Trained model persistence using Joblib
- REST API for real-time recommendations
- Scalable architecture for future extensions
- Offline training with online inference support

---

## 🏗️ System Architecture

```
KKBOX Dataset
   ↓
Data Cleaning & EDA
   ↓
User–Item Interaction Matrix
   ↓
ALS Model Training (Implicit Collaborative Filtering)
   ↓
Top-N Recommendation Generation
   ↓
Model Serialization
   ↓
REST API
   ↓
User Receives Recommendations
```

---

## 🧩 Tech Stack

| Layer | Technology |
|------|------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| ML Library | Surprise |
| Model Storage | Joblib |
| API | Flask / FastAPI |
| Version Control | Git & GitHub |

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-lightblue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Recommender-brightgreen)
![Surprise](https://img.shields.io/badge/Surprise-Recommendation%20Library-orange)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Storage-yellow)
![API](https://img.shields.io/badge/API-Flask%20%2F%20FastAPI-red)
![Git](https://img.shields.io/badge/Git-Version%20Control-black)
![GitHub](https://img.shields.io/badge/GitHub-Code%20Hosting-purple)

---

## 📁 Project Structure

```
music-recommendation-system/
├── api/            
├── data/           
├── model/          
├── notebooks/      
├── .gitignore
├── README.md
└── requirements.txt
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