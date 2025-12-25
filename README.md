# 🎬 Movie Recommendation System

This is a movie recommendation system built using Python and Machine Learning.

## 🔹 Features
- Recommends movies based on similarity
- Uses cosine similarity
- Simple and interactive UI with Streamlit

## 🔹 Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
  
## 🔹 How to Run the Project

### 1️⃣ Install required libraries
```bash
pip install streamlit pandas numpy scikit-learn requests
```

### 2️⃣ Dataset Information
The dataset used for this project is large and exceeds GitHub's file size limit, so it is not included in this repository.

To run this project:
- Download the TMDB movies and credits dataset
- Place `tmbd_movies.csv` and `tmbd_credits.csv` in the project root folder

### 3️⃣ Run backend (one time)
```bash
python backend.py
```

### 4️⃣ Run the application
```bash
streamlit run app.py
```

## 🔹 Project Flow
- `backend.py` preprocesses the data and computes movie similarity
- `app.py` provides an interactive Streamlit interface

## 📂 Dataset Information

The dataset used for this project is large and exceeds GitHub's file size limit, so it is not included in this repository.

To run this project:
- Download the TMDB movies and credits dataset
- Place `tmbd_movies.csv` and `tmbd_credits.csv` in the project root folder
- Then run `backend.py` followed by `app.py`

The complete preprocessing and recommendation logic is included in the code.

