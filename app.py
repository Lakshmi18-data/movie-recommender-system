import streamlit as st
import pickle
import pandas as pd


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])


    recommended_movie=[]

    for i in distances[1:6]:
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity (1).pkl','rb'))



st.title('MOVIE RECOMMENDER SYSTEM')

selected_movie_name= st.selectbox(
'how would u like to  be contacted',
movies['title'].values)

if st.button('Recommend'):
    recommmendations =recommend(selected_movie_name)
    for i in recommmendations:
        st.write(i)
