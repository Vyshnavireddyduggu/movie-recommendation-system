import streamlit as st
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


import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommendation System")

st.title("🎬 Movie Recommendation System")

# =========================
# LOAD MOVIE DATA
# =========================
movies = pickle.load(open('movie_list.pkl', 'rb'))
# =========================
# CREATE SIMILARITY (NO .pkl FILE NEEDED)
# =========================
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

# =========================
# RECOMMEND FUNCTION
# =========================
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations

# =========================
# UI
# =========================
selected_movie = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    results = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for movie in results:
        st.write("👉", movie)





