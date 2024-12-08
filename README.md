The Movie Recommendation System is a personalized content recommendation platform developed using Python and Streamlit. It leverages advanced Natural Language Processing (NLP) techniques and machine learning algorithms to suggest movies based on user preferences.

The backend integrates multiple libraries such as Pandas for data manipulation, Scikit-learn for cosine similarity calculations, and CountVectorizer for text vectorization. A dataset of movies and metadata (including genres, cast, crew, and keywords) was preprocessed to generate feature vectors. Cosine similarity was then used to compare movie tags and rank recommendations.

The frontend is designed with Streamlit, offering a simple and interactive user interface. Users can select a movie, and the system provides five recommendations, accompanied by movie posters fetched via The Movie Database (TMDb) API.

Key Features:

Data cleaning and preprocessing using Python.
Content-based filtering using Cosine Similarity.
NLP with Porter Stemmer to normalize text data.
Real-time integration of TMDb API for fetching posters.
A sleek, user-friendly interface styled with CSS via Streamlit.
This project serves as a practical application of data science, machine learning, and web development skills, demonstrating how AI can enhance user experiences in entertainment.

