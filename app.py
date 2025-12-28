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
st.markdown("""
<style>
/* Main background */
.stApp {
    background-image: url("https://wallpapercave.com/wp/wp1917154.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Dark overlay for readability */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(120, 0, 0, 0.65);
    z-index: -1;
}

/* Title */
h1 {
    color: white;
    text-shadow: 2px 2px 8px black;
}

/* Select box background */
div[data-baseweb="select"] > div {
    background-color: white !important;
}

/* Select box text */
div[data-baseweb="select"] span {
    color: black !important;
    font-weight: 500;
}

/* Dropdown options */
ul li {
    color: black !important;
}

/* Labels */
label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


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

