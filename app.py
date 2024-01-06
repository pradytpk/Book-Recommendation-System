import pickle
import streamlit as st
import numpy as np

def recommended_books(book_name):
    book_list=[]
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list,poster_url

def fetch_poster(suggestion):
    book_names=[]
    ids_index=[]
    poster_url=[]

    for book_id in suggestion:
        book_names.append(book_pivot.index[book_id])


    for name in book_names[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)
    
    return poster_url



st.header("Book Recommendation System")
model = pickle.load(open('artifacts/model.pk1','rb'))
books_name = pickle.load(open('artifacts/books_name.pk1','rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pk1','rb'))
final_rating = pickle.load(open('artifacts/final_rating.pk1','rb'))


selected_books = st.selectbox("Type or select a books",books_name)

if st.button('Show Recommendation'):
    recommedation_books, poster_url = recommended_books(selected_books)
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(recommedation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommedation_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommedation_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommedation_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommedation_books[5])
        st.image(poster_url[5])
