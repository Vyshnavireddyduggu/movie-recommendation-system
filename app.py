import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

# =========================
# STRANGER THINGS RED THEME + GLOW TITLE
# =========================
st.markdown("""
<style>

/* Background */
.stApp {
    background-image: url("https://wallpapercave.com/wp/wp1917154.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Dark red overlay */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(90, 0, 0, 0.7);
    z-index: -1;
}

/* Glowing title animation */
@keyframes glow {
    0% {
        text-shadow: 0 0 5px #ff0000;
    }
    50% {
        text-shadow: 0 0 20px #ff1a1a, 0 0 40px #ff3333;
    }
    100% {
        text-shadow: 0 0 5px #ff0000;
    }
}

.glow-title {
    font-size: 60px;
    font-weight: 900;
    color: #ff0000;
    text-align: center;
    animation: glow 2s infinite;
    margin-bottom: 30px;
}

/* Labels */
label {
    color: white !important;
    font-weight: 600;
}

/* Select box */
div[data-baseweb="select"] > div {
    background-color: white !important;
}

div[data-baseweb="select"] span {
    color: black !important;
    font-weight: 500;
}

/* Dropdown options */
ul li {
    color: black !important;
}

/* Recommend button */
.stButton > button {
    background-color: #ff0000;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 8px;
    padding: 8px 25px;
}

.stButton > button:hover {
    background-color: #cc0000;
}

/* Movie name text */
.movie-title {
    color: white;
    text-align: center;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
#️# =========================
st.markdown(
    '<h1 class="glow-title">🎬 Movie Recommendation System</h1>',
    unsafe_allow_html=True
)

# =========================
# LOAD MOVIE DATA
# =========================
movies = pickle.load(open("movie_list.pkl", "rb"))

# =========================
# CREATE SIMILARITY (NO similarity.pkl)
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

    names, posters = [], []

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
            if posters[i]:
                st.image(posters[i], use_container_width=True)
            st.markdown(
                f"<p class='movie-title'>{names[i]}</p>",
                unsafe_allow_html=True
            )
