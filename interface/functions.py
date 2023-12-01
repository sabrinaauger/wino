# Many imports for functions for other pages, but also a few for similar semantics for tokens
import json
import pandas as pd
import streamlit as st
from interface.data import load_data, load_type, load_country, load_price, load_designation
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
    # Load data then get the country column from df
    df = load_country(load_data())

    # Display a region selector widget using Streamlit
    selected_country = st.selectbox("Select your preferred country:", df.unique())
    return selected_country

# This is base suggest_wines() with price and country only
def suggest_wines():
    # Access variables from the global scope
    price_range = global_price_range
    wine_preference = global_wine_preference
    selected_country = global_country
    aroma_options = global_aroma_options

    # Loading dataset as needed to find the right suggestion
    df = load_data()
    price_column= load_price(df)


    # Filter the main dataset with the given input the user has given
    suggestion_df = df[
        (load_country(df) == selected_country) &
        (price_column >= price_range[0]) &
        (price_column <= price_range[1]) &
        (load_type(df) == wine_preference)
    ]

    # Ensure there are at least 3 suggestions
    if not suggestion_df.empty:
        # Sort the dataset based on 'points' in descending order
        suggestion_df = suggestion_df.sort_values(by='points', ascending=False)

        # Extract wine varieties, descriptions, and prices from the filtered and sorted dataset
        recommendations = load_designation(suggestion_df).unique()[:3].tolist()
        descriptions = suggestion_df['description'][:3].tolist()
        prices = suggestion_df['price'][:3].tolist()
    else:
        # If no wines match the criteria, provide a generic suggestion for each element
        recommendations = ["No matching options available. Please try again 🍷."]
        descriptions = ["No matching options available. Please try again 🍷."]
        prices = ["No matching options available. Please try again 🍷."]

    return recommendations, descriptions, prices

#Once the survey has been submitted...
def submit_survey(price_range, wine_preference, selected_country, aroma_options):
    #...we store the variables in our global variables to be used across the pages
    set_global_variables(price_range,wine_preference, selected_country, aroma_options)
    #set to result to go to result page
    st.session_state.page = 'result'

# Define the show additional suggestions button function with an initial state
def suggest_button():
    label = "Hide additional suggestions" if st.session_state.show_additional_suggestions else "Show additional suggestions"
    return st.button("Show additional suggestions", key="additional_suggestions_button", on_click=suggest_set)

# Function to toggle the state of additional suggestions
def suggest_set():
    st.session_state.show_additional_suggestions = not st.session_state.show_additional_suggestions
    return st.session_state.show_additional_suggestions


#Define the redo survey button
def redo_survey():
    st.button("Redo the survey", on_click=set_page_to_welcome)
