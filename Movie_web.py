import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def movie_recommend(movie):
    index=list_movies[list_movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    recommended_movie_posters = []
    for i in distance[0:6]:
         # fetch the movie poster
        movie_id=list_movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(list_movies.iloc[i[0]].title)
    return recommended_movies,recommended_movie_posters

st.header("Movie Recommender System")
list_movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=list_movies['title'].values

movie = st.selectbox(
    'Type or select a movie from the dropdown',
    movies_list)

if st.button('Recommend'):
    # recommendations=movie_recommend(movie)
    # for i in recommendations:
    #     st.write(i)
    recommended_movies,recommended_movie_posters = movie_recommend(movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movie_posters[4])
