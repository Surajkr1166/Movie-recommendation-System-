import streamlit as st

import pickle

import pandas as pd

import requests




def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6335ec3a2541202257abdad5b6ef9729&language=en-US'.format(movie_id))
    data=response.json()


    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch the poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity_dict.pkl','rb'))



st.title('🎬Movie Recommender System')
# Add background color and styling to the entire page
# Add background color and styling to the entire page
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;  /* White background for the whole page */
        color: #333333;  /* Dark gray text color for better contrast */
    }

    .stButton > button {
        background-color: #FFD700;  /* Yellow button background */
        color: black;  /* Black text color for the button */
        padding: 10px 24px;
        border-radius: 5px;
        font-size: 16px;
    }

    .stButton > button:hover {
        background-color: #FFCC00;  /* Darker yellow on hover */
    }

    .stSelectbox > div, .stTextInput > div {
        background-color: #F7F7F7;  /* Light gray background for input boxes */
        color: #333333;  /* Dark gray text color for inputs */
    }

    .stTextInput > div > input {
        color: #333333;  /* Dark text color inside input fields */
    }

    .stSelectbox > div > div > div {
        background-color: #F7F7F7;  /* Light gray dropdown background */
    }

    </style>
    """, unsafe_allow_html=True
)

st.subheader("Select a movie to get recommendations:")

selected_movie_name = st.selectbox(
    'How would you like to be connected?',
    movies['title'].values)

# Recommendation Button
if st.button('Recommend Movies'):
    names, posters = recommend(selected_movie_name)

    if names:
        st.subheader(f"Recommendations for **{selected_movie_name}**:")
        # Display posters and names in a single frame
        cols = st.columns(len(names))  # Create a column for each recommendation
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.image(poster, use_container_width=True)  # Display the poster
                st.text(name)  # Display the name
    else:
        st.error("Sorry, no recommendations could be generated. Please try another movie.")
else:
    st.info("Select a movie and click 'Recommend Movies' to get started!")
