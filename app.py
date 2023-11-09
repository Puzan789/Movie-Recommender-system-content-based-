import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import requests

movies_list=pickle.load(open('recc.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
def recommend_movie(movie_name):
    indexx=movies[movies['title']==movie_name].index[0]
    distance=similarity[indexx]
    movies_lists= sorted(list(enumerate(distance)),reverse=True,key = lambda x: x[1])[1:6]
    name=[]
    recommended_movies_poster=[]
    for i in movies_lists:
        movie_id=movies.iloc[i[0]].id
        name.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return name,recommended_movies_poster
    
st.title("Movie Recommender System")
option = st.selectbox(
    'Which movie you watched recently?',
    movies['title'].values)

st.write('You selected:',option) 

if st.button('Recommend'):
    names,poster=recommend_movie(option)
    st.title("The recommended movies are:")

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.write(names[0])
        st.image(poster[0])

    with col2:
        st.write(names[1])
        st.image(poster[1])

    with col3 :
        st.write(names[2])
        st.image(poster[2])
    with col4:
        st.write(names[3])
        st.image(poster[3])
    with col5:
        st.write(names[4])
        st.image(poster[4])
