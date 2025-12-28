# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python** and **Machine Learning**, which recommends similar movies based on user selection.  
The project demonstrates an end-to-end ML pipeline including data preprocessing, feature extraction, similarity computation, and deployment using Streamlit.

---

## 📌 Project Overview

Recommendation systems are widely used by platforms like Netflix, Amazon, and Spotify.  
This project implements a **content-based recommendation system** that suggests movies similar to a selected movie using **cosine similarity** on movie metadata.

The application is deployed using **Streamlit**, providing a simple and interactive user interface.

---

## ✨ Features

- Recommends top 5 similar movies
- Content-based filtering approach
- Uses cosine similarity for recommendation
- Interactive web interface using Streamlit
- Deployed as a live web application

---

## 🧠 Algorithm Used

- Content-Based Recommendation System
- CountVectorizer for text vectorization
- Cosine Similarity to calculate similarity between movies

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- TMDB API

---

## 🔄 Project Workflow

1. Load TMDB movies and credits dataset  
2. Merge and clean the datasets  
3. Extract important features such as:
   - Genres
   - Keywords
   - Cast
   - Crew
4. Combine features into a single `tags` column  
5. Convert text data into numerical vectors using CountVectorizer  
6. Compute cosine similarity between movies  
7. Recommend top 5 similar movies based on user selection  
8. Display recommendations using Streamlit UI  

---

## 📂 Project Structure
Movie-Recommendation-System/
│
├── backend.py # Data preprocessing and similarity computation
├── app.py # Streamlit application
├── movie_list.pkl # Preprocessed movie data
├── similarity.pkl # Similarity matrix
├── requirements.txt
└── README.md


---

## 📊 Dataset Information

The dataset used in this project is sourced from **TMDB (The Movie Database)**.

⚠️ **Note:**  
The dataset files are large and exceed GitHub’s file size limit, so they are not included in this repository.

### To run the project locally:
- Download the TMDB movies and credits dataset
- Place the following files in the project root directory:
  - `tmbd_movies.csv`
  - `tmbd_credits.csv`

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install streamlit pandas numpy scikit-learn requests


2️⃣ Run Backend (One-Time)

This step preprocesses the data and generates the similarity matrix.
python backend.py

3️⃣ Run the Streamlit Application

streamlit run app.py


## 🔗 Live Demo
👉 https://movie-recommendation-system-6kqx5vqfmqf5hmvsufiuc3.streamlit.app
## 🎯 What I Learned from This Project

- Building a content-based recommendation system  
- Text preprocessing and feature engineering  
- Applying NLP techniques for real-world problems  
- Using cosine similarity for recommendations  
- Working with large datasets efficiently  
- Deploying machine learning applications using Streamlit  
- Structuring ML projects in a clean and modular way  

---

## 🚀 Future Enhancements

- Implement collaborative filtering  
- Use TF-IDF instead of CountVectorizer  
- Add user authentication and personalized recommendations  
- Include movie ratings and trailers  
- Improve performance for large-scale datasets  



## 👩‍💻 Author

**Vyshnavi Reddy**  
B.Tech Student | Aspiring Software & ML Engineer  






