# Many imports for functions for other pages, but also a few for similar semantics for tokens
import json
import pandas as pd
import streamlit as st
from interface.data import load_country
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

# Load Word2Vec model
# model_path = 'path/to/your/word2vec/model.bin'
# word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

#Set page to survey
def set_page_to_survey():
    st.session_state.page = 'survey'
#set page to welcome
def set_page_to_welcome():
    st.session_state.page = 'welcome'

#store the variables in our global variables to be used across the pages
def set_global_variables(price_range, wine_preference, selected_country, aroma_options):
    global global_price_range
    global global_wine_preference
    global global_country
    global global_aroma_options

    global_price_range = price_range
    global_wine_preference = wine_preference
    global_country = selected_country
    global_aroma_options = aroma_options

# Region selector function
def country_selector():
    # Use the load_country function from data.py
    df = load_country()

    # Display a region selector widget using Streamlit
    selected_country = st.selectbox("Select your preferred country:", df.unique())
    return selected_country

# # This is base code + Word2Vec
# def suggest_wines():
#     # Access variables from the global scope
#     price_range = global_price_range
#     wine_preference = global_wine_preference
#     selected_country = global_country
#     aroma_options = global_aroma_options

#     recommendations = []

#     # Loading dataset as needed to find the right suggestion
#     dataset_path = '~/code/sabrinaauger/wino/raw_data/winemag-data_first150k.csv'
#     wine_df = pd.read_csv(dataset_path)

#     # Load aroma options data from JSON files
#     aroma_keywords = []
#     for aroma_option in aroma_options:
#         aroma_file_path = f'aromas/{aroma_option.lower()}.json'
#         with open(aroma_file_path, 'r') as f:
#             aroma_data = json.load(f)
#             aroma_keywords.extend(aroma_data)

#     # We filter the main dataset with the given input the user has given
#     suggestion_df = wine_df[
#         (wine_df['country'] == selected_country) &
#         (wine_df['price'] >= price_range[0]) &
#         (wine_df['price'] <= price_range[1])
#     ]

#     # Ensure there are at least 3 suggestions
#     if not suggestion_df.empty:
#         # Filter the dataset based on semantic similarity in 'description' column
#         matching_wines = []
#         for _, wine_row in suggestion_df.iterrows():
#             description_words = set(wine_row['description'].lower().split())
#             for aroma_keyword in aroma_keywords:
#                 if any(word in word2vec_model and word2vec_model.similarity(word, aroma_keyword) > 0.7 for word in description_words):
#                     matching_wines.append(wine_row['variety'])
#                     break

#             if len(matching_wines) >= 3:
#                 break

#         recommendations = matching_wines[:3] if matching_wines else ["No available options. Please retry 🍷."]
#     else:
#         # If no wines match the criteria, provide a generic suggestion
#         recommendations = [f"No wines found in the specified price range and country ({selected_country}, {price_range[0]} - {price_range[1]})"]

#     return recommendations

# This is base suggest_wines() with price and country only
def suggest_wines():
    # Access variables from the global scope
    price_range = global_price_range
    wine_preference = global_wine_preference
    selected_country = global_country
    aroma_options = global_aroma_options

    # Loading dataset as needed to find the right suggestion
    dataset_path = '~/code/sabrinaauger/wino/interface/wine_reviews.csv'
    wine_df = pd.read_csv(dataset_path)

    # Filter the main dataset with the given input the user has given
    suggestion_df = wine_df[(wine_df['country'] == selected_country) & (wine_df['price'] >= price_range[0]) & (wine_df['price'] <= price_range[1])]

    recommendations = []

    # Ensure there are at least 3 suggestions
    if not suggestion_df.empty:
        # Sort the dataset based on 'points' in descending order
        suggestion_df = suggestion_df.sort_values(by='points', ascending=False)

        # Extract wine varieties from the filtered and sorted dataset
        recommendations = suggestion_df['variety'].unique()[:3].tolist()
    else:
        # If no wines match the criteria, provide a generic suggestion
        recommendations = ["No matching options available. Please try again 🍷."]

    return recommendations


#Once the survey has been submitted...
def submit_survey(price_range, wine_preference, selected_country, aroma_options):
    #...we store the variables in our global variables to be used across the pages
    set_global_variables(price_range,wine_preference, selected_country, aroma_options)
    #set to result to go to result page
    st.session_state.page = 'result'
