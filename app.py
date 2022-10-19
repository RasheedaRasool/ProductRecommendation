import pickle
import streamlit as st
import requests

def fetch_poster(prod_id):
    url = "https://api.theproddb.org/3/prod/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(prod_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(prod):
    index = df[df['product'] == prod].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_prod_names = []
    recommended_prod_posters = []
    for i in distances[1:6]:
        # fetch the prod poster
        prod_id = df.iloc[i[0]].prod_id
        recommended_prod_posters.append(fetch_poster(prod_id))
        recommended_prod_names.append(df.iloc[i[0]].product)

    return recommended_prod_names,recommended_prod_posters


st.header('Product Recommender System')
df = pickle.load(open('product.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

prod_list = df['product'].values
selected_prod = st.selectbox(
    "Type or select a prod from the dropdown",
    prod_list
)

if st.button('Show Recommendation'):
    recommended_prod_names,recommended_prod_posters = recommend(selected_prod)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_prod_names[0])
        st.image(recommended_prod_posters[0])
    with col2:
        st.text(recommended_prod_names[1])
        st.image(recommended_prod_posters[1])

    with col3:
        st.text(recommended_prod_names[2])
        st.image(recommended_prod_posters[2])
    with col4:
        st.text(recommended_prod_names[3])
        st.image(recommended_prod_posters[3])
    with col5:
        st.text(recommended_prod_names[4])
        st.image(recommended_prod_posters[4])





