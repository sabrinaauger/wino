#variables flavour are currently placeholders, need to add more options depending on data
import json
import pandas as pd
import streamlit as st
from interface.data import load_country

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


def suggest_wines():
    # Access variables from the global scope
    price_range = global_price_range
    wine_preference = global_wine_preference
    selected_country = global_country
    aroma_options = global_aroma_options

    # Loading dataset as needed to find the right suggestion
    dataset_path = '~/code/sabrinaauger/wino/raw_data/winemag-data_first150k.csv'
    wine_df = pd.read_csv(dataset_path)

    # Filter the main dataset with the given input the user has given
    suggestion_df = wine_df[(wine_df['country'] == selected_country) & (wine_df['price'] >= price_range[0]) & (wine_df['price'] <= price_range[1])]

    recommendations = []

    # Ensure there are at least 3 suggestions
    if not suggestion_df.empty:
        # Extract wine varieties from the filtered dataset
        recommendations = suggestion_df['variety'][:3].tolist()
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


    # Basic recommendation logic based on user's preferences,replace with actual model when ready
    # if wine_preference == 'Red':
    #     if 'Fruity' in aroma_options:
    #         recommendations.append("Zinfandel (Fruity, Sweet)")
    #     if 'Earthy' in aroma_options:
    #         recommendations.append("Shiraz (Earthy, Dry)")
    # elif wine_preference == 'White':
    #     if 'Floral' in aroma_options:
    #         recommendations.append("Moscato (Floral, Sweet)")
    #     if 'Herbal' in aroma_options:
    #         recommendations.append("Chardonnay (Herbal, Dry)")

    # Further refinement based on price range
    # min_price, max_price = price_range
    # if min_price < 20:
    #     recommendations.append("Affordable Choice: Chardonnay")
    # elif min_price >= 20 and max_price <= 50:
    #     recommendations.append("Mid-Range Choice: Pinot Noir")
    # elif max_price > 50:
    #     recommendations.append("Premium Choice: Cabernet Sauvignon")
