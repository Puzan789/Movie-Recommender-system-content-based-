

# Movie Recommender System

Welcome to the **Movie Recommender System** repository! This project is a simple and intuitive application that suggests movies based on a user’s recent watch. Built using Streamlit, this app leverages a pre-trained model to recommend movies and displays their posters for easy browsing.

## Features

- **Movie Recommendations**: Suggests five movies similar to the one selected by the user.
- **Poster Display**: Fetches and displays movie posters to provide a visual appeal and help users choose their next watch.
- **User-Friendly Interface**: Built with Streamlit, offering a seamless and interactive user experience.

## How It Works

1. **Data Loading**: The system loads a pre-trained movie similarity model and a dataset containing movie details.
2. **Movie Selection**: The user selects a movie they’ve recently watched from a dropdown menu.
3. **Recommendation Engine**: Upon selection, the system calculates the similarity scores between the selected movie and other movies in the dataset.
4. **Poster Retrieval**: The system fetches posters for the recommended movies using The Movie Database (TMDb) API.
5. **Display**: The recommended movie titles and posters are displayed side by side for easy viewing.

## Requirements

- Python 3.8 or above
- Streamlit
- Pandas
- NumPy
- Requests


## Usage

1. **Select a Movie**: Use the dropdown menu to select a movie you’ve recently watched.
2. **Get Recommendations**: Click the "Recommend" button to receive five movie recommendations.
3. **Explore**: Browse the recommended movies along with their posters to decide your next watch.

## Key Components

- **Pre-trained Model**: The `recc.pkl` file contains a list of movies and their features used for recommendation.
- **Similarity Matrix**: The `similarity.pkl` file is a precomputed similarity matrix that helps find movies similar to the selected one.
- **TMDb API**: Used to fetch movie posters, enhancing the visual experience.


 #### Dataset Link : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
 #### Streamlit documentation  : https://docs.streamlit.io/library/get-started

 ## Final Output :
 ![Screenshot (70)](https://github.com/Puzan789/Movie-Recommender-system-content-based-/assets/100143567/c092e91a-ec65-47df-b69d-e5d22a85e342)

 ## My other machine learning projects topic wise: https://github.com/Puzan789/ML-projects-of-separates-topics
