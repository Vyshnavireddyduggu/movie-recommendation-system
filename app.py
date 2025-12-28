import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Movie Recommendation System")

# =========================
# RED STRANGER THINGS BACKGROUND
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background-image:
            linear-gradient(rgba(139,0,0,0.75), rgba(139,0,0,0.75)),
            url("https://wallpaperaccess.com/full/1097137.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    h1, h2, h3, label, span, div, p {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎬 Movie Recommendation System")

# =========================
# LOAD MOVIE DATA
# =========================
movies = pickle.load(open("movie_list.pkl", "rb"))

# =========================
# CREATE SIMILARITY
# =========================
cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(movies["tags"]).toarray()
similarity = cosine_similarity(vectors)

# =========================
# TMDB POSTER FUNCTION
# =========================
def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

# =========================
# RECOMMEND FUNCTION
# =========================
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters

# =========================
# UI
# =========================
selected_movie = st.selectbox(
    "Select a movie:",
    movies["title"].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    st.subheader("Recommended Movies")

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.write(names[i])
