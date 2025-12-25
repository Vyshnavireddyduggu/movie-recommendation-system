import pandas as pd
import ast
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ===============================
# LOAD DATA (SAFE MODE)
# ===============================
movies = pd.read_csv('tmbd_movies.csv', low_memory=False)
credits = pd.read_csv('tmbd_credits.csv', low_memory=False)

# ===============================
# MERGE DATA
# ===============================
movies = movies.merge(credits, on='title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

# ===============================
# HELPER FUNCTIONS (SAFE)
# ===============================
def convert(text):
    try:
        return [i['name'] for i in ast.literal_eval(text)]
    except:
        return []

def collapse(L):
    return [i.replace(" ", "") for i in L]

# ===============================
# DATA PROCESSING
# ===============================
movies['genres'] = movies['genres'].apply(convert).apply(collapse)
movies['keywords'] = movies['keywords'].apply(convert).apply(collapse)
movies['cast'] = movies['cast'].apply(convert).apply(lambda x: x[:3]).apply(collapse)
movies['crew'] = movies['crew'].apply(convert).apply(collapse)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

movies['tags'] = (
    movies['overview']
    + movies['genres']
    + movies['keywords']
    + movies['cast']
    + movies['crew']
)

new = movies[['movie_id', 'title', 'tags']]
new['tags'] = new['tags'].apply(lambda x: " ".join(x))

# ===============================
# VECTORIZE & SIMILARITY
# ===============================
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new['tags']).toarray()
similarity = cosine_similarity(vector)

# ===============================
# SAVE FILES
# ===============================
pickle.dump(new, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ backend.py executed successfully")
