import streamlit as st
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction import text

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")
st.write("Find similar movies using NLP (TF-IDF) and KNN Algorithm")

# ----------------------------
# LOAD DATA
# ----------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("movies.csv")

    df['Duration'] = df['Duration'].fillna("-")
    df['Ratings'] = df['Ratings'].str.replace("N/a","0")

    df["Film Name"] = df['Film Name'].str.replace(
        r"[^a-zA-Z\s]","",regex=True
    )

    df = df.dropna(subset=["Summary"])
    df = df.reset_index(drop=True)

    df["Summary"] = df["Summary"].str.lower()
    df["Summary"] = df["Summary"].str.strip()

    return df


df = load_data()

# ----------------------------
# NLP MODEL
# ----------------------------

tfidf = TfidfVectorizer(stop_words="english")
tf_matrix = tfidf.fit_transform(df["Summary"])

knn = NearestNeighbors(
    n_neighbors=6,
    metric="cosine",
    algorithm="brute"
)

knn.fit(tf_matrix)

# ----------------------------
# RECOMMEND FUNCTION
# ----------------------------

def recommendation(movie_name):

    movie_name = movie_name.lower()
    movie_list = df['Film Name'].str.lower().str.strip().values

    if movie_name not in movie_list:
        return None

    index = df[df['Film Name'].str.lower().str.strip()==movie_name].index[0]

    distance, indice = knn.kneighbors(tf_matrix[index])

    recommended_movies = []

    for i in range(1,len(indice[0])):

        movie_index = indice[0][i]

        name = df.iloc[movie_index]["Film Name"]
        rating = df.iloc[movie_index]["Ratings"]
        year = df.iloc[movie_index]["Year"]

        recommended_movies.append((name,rating,year))

    return recommended_movies


# ----------------------------
# USER INPUT
# ----------------------------

movie_input = st.text_input("Enter Movie Name")

if st.button("Get Recommendations"):

    result = recommendation(movie_input)

    if result is None:
        st.error("Movie not found in dataset")
    else:
        st.success("Recommended Movies 🎬")

        for movie in result:
            st.write(f"🎬 **{movie[0]}** | ⭐ Rating: {movie[1]} | 📅 Year: {movie[2]}")


# ----------------------------
# DATA PREVIEW
# ----------------------------

with st.expander("View Dataset"):
    st.dataframe(df.head())