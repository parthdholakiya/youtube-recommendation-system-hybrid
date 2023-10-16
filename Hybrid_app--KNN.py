import streamlit as st
import pickle
import pandas as pd
import joblib



# Define the hybrid recommender function
def hybrid(title):
    index = new[new['title'] == title].index[0]
    query_vector = vector[index].reshape(1, -1)
    distances, indices = knn_model.kneighbors(query_vector)

    # Extract the indices of the recommended videos (excluding the query itself)
    video_indices = indices[0][1:6]
    
    # Use .iloc to select rows by integer position from the 'smd' DataFrame
    recommended_videos = smd.iloc[video_indices][['title', 'categoryId', 'video_id', 'likes','thumbnail_link']]
    
    # Calculate the 'est' value for each recommended video based on user preferences
    recommended_videos['est'] = recommended_videos['categoryId'].apply(lambda x: knn_baseline.predict(1, indices_map.iloc[x]['video_id']).est)
    
    # Sort the recommended videos by the number of likes in descending order
    recommended_videos = recommended_videos.sort_values('likes', ascending=False)
    
    recomend_video = recommended_videos[['title','thumbnail_link']].values.tolist()
    return recomend_video

# Load the necessary data
smd = joblib.load(open('smd.pkl','rb'))

new = joblib.load(open('new.pkl','rb'))

vector = joblib.load(open('vector.pkl','rb'))

indices_map= joblib.load(open('indices_map.pkl','rb'))

#indices = joblib.load(open('indices.pkl','rb'))

knn_baseline = joblib.load(open('KNNBaseline.pkl','rb'))

knn_model = joblib.load(open('KNN_model.pkl','rb'))

# Set up the app layout
st.set_page_config(page_title='YouTube recommendation System', page_icon=':tv:', layout='wide')
st.title('YouTube recommendation System')
st.markdown("""
"Discover new videos that match your interests. Simply choose a video from the dropdown list and click the 'Show Recommendation' button to start exploring! You can also look for videos related to topics like Modi, BTS, Apple iPhone 12 Pro, and Gujarati songs. Enjoy finding videos that suit your preferences!"
""")

# Create the video selection dropdown
video_list = smd['title'].values
selected_video = st.selectbox(
    "Select a video",
    video_list
)

# Create the "Show Recommendation" button and display the recommended videos
if st.button('Show Recommendation'):
    recomend_video = hybrid(selected_video)
    cols = st.columns(4)
    for i, col in enumerate(cols):
        with col:
            if i < len(recomend_video):
                st.image(recomend_video[i][1], use_column_width=True)
                st.subheader(recomend_video[i][0])
            else:
                break

# Add a footer with some information about the project and its creator
st.markdown("""
    ---
    **This project is a hybrid YouTube recommender system designed to suggest videos similar to the one chosen by the user. It employs a blend of content-based and collaborative filtering techniques. The content-based aspect relies on video tags and uses the K-Nearest Neighbors (KNN) algorithm to make recommendations. On the other hand, the collaborative filtering component takes into account user preferences, specifically their likes, and utilizes algorithms based on a modified nearest neighbors approach, such as KNNBaseline, to predict likes and generate personalized recommendations.
    
""")

# Add a sidebar with the YouTube logo and some information about the project creator
st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/1200px-YouTube_Logo_2017.svg.png', width=200)
st.sidebar.markdown("""
    **Created by:** Parth N Dholakiya
    This project was created as part of NLP course at Purdue University.
    Contact me at parthdholakiya180@gmail.com for more information.
""")

