# YouTube Recommendation System

![YouTube Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/1200px-YouTube_Logo_2017.svg.png)

## Overview

This project is a hybrid YouTube recommender system designed to suggest videos similar to the one chosen by the user. It combines content-based and collaborative filtering techniques to provide personalized video recommendations. The content-based aspect relies on video tags and uses the K-Nearest Neighbors (KNN) algorithm, while the collaborative filtering component takes into account user preferences, specifically their likes, and utilizes algorithms like KNNBaseline.

## Getting Started

To run the project locally, follow these steps:

1. Install the required dependencies:

    ```bash
    pip install streamlit pandas scikit-learn
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/parthdholakiya/youtube-recommendation-system-hybrid.git
    ```

3. Navigate to the project directory:

    ```bash
    cd YouTube-Recommendation-System
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run Hybrid_YouTube Recom_app.py
    ```

5. Open your browser and go to [http://localhost:8501](http://localhost:8501) to interact with the recommendation system.

## Usage

1. Choose a video from the dropdown list.
2. Click the 'Show Recommendation' button to get personalized video recommendations.
3. Explore and discover new videos that match your interests.

## Project Structure

- `app.py`: Streamlit app script.
- `smd.pkl`: Serialized file containing necessary data for the recommender system.
- `new.pkl`: Serialized file containing additional data for the recommender system.
- `vector.pkl`: Serialized file containing vector data for the recommender system.
- `indices_map.pkl`: Serialized file containing mapping indices for the recommender system.
- `KNNBaseline.pkl`: Serialized file containing the trained KNNBaseline model.
- `KNN_model.pkl`: Serialized file containing the trained KNN model.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)

## About the Creator

**Parth N Dholakiya**

- Email: parthdholakiya180@gmail.com

This project was created as part of the NLP course at Purdue University.

## Acknowledgments

Special thanks to the creators of the [Streamlit](https://streamlit.io/) library and the [scikit-learn](https://scikit-learn.org/) machine learning library for their valuable tools.

![image](https://user-images.githubusercontent.com/94167271/235462664-7eb4da42-3371-445b-97f2-f3908e840636.png)

demo app - http://ec2-54-219-96-177.us-west-1.compute.amazonaws.com:8501/ 

![Screenshot (438)](https://github.com/parthdholakiya/youtube-recommendation-system-hybrid/assets/94167271/cf1f571f-3bdf-4b51-9999-218d397d6b8e)
