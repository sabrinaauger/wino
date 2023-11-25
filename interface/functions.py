#variables flavour and dryness are currently placeholders, need to add more options depending on data

import streamlit as st
from interface.data import load_country

#Set page to survey
def set_page_to_survey():
    st.session_state.page = 'survey'
#set page to welcome
def set_page_to_welcome():
    st.session_state.page = 'welcome'

#store the variables in our global variables to be used across the pages
def set_global_variables(price_range, wine_preference, selected_country, flavour_options, dryness_options):
    global global_price_range
    global global_wine_preference
    global global_country
    global global_flavour_options
    global global_dryness_options

    global_price_range = price_range
    global_wine_preference = wine_preference
    global_country = selected_country
    global_flavour_options = flavour_options
    global_dryness_options = dryness_options

# select country
def country_selector():
    df = load_country()  # Load the dataset

    # Display a country selector widget using Streamlit
    selected_country = st.selectbox("Select a country:", df.unique())

    return selected_country

def suggest_wines():
    # Access variables from the global scope
    price_range = global_price_range
    wine_preference = global_wine_preference
    selected_country = global_country
    flavour_options = global_flavour_options
    dryness_options = global_dryness_options

    recommendations = []

    # Basic recommendation logic based on user's preferences,replace with actual model when ready
    if wine_preference == 'Red':
        if 'Fruity' in flavour_options and 'Sweet' in dryness_options:
            recommendations.append("Zinfandel (Fruity, Sweet)")
        if 'Earthy' in flavour_options and 'Dry' in dryness_options:
            recommendations.append("Shiraz (Earthy, Dry)")
    elif wine_preference == 'White':
        if 'Floral' in flavour_options and 'Sweet' in dryness_options:
            recommendations.append("Moscato (Floral, Sweet)")
        if 'Herbal' in flavour_options and 'Dry' in dryness_options:
            recommendations.append("Chardonnay (Herbal, Dry)")

    # Further refinement based on price range
    min_price, max_price = price_range
    if min_price < 20:
        recommendations.append("Affordable Choice: Chardonnay")
    elif min_price >= 20 and max_price <= 50:
        recommendations.append("Mid-Range Choice: Pinot Noir")
    elif max_price > 50:
        recommendations.append("Premium Choice: Cabernet Sauvignon")

    # Ensure there are at least 3 suggestions
    while len(recommendations) < 3:
        recommendations.append(f"Generic Wine Choice from {selected_country}")

    return recommendations


#Once the survey has been submitted...
def submit_survey(price_range, wine_preference, selected_country, flavour_options, dryness_options):
    #...we store the variables in our global variables to be used across the pages
    set_global_variables(price_range,wine_preference, selected_country, flavour_options, dryness_options)
    #set to result to go to result page
    st.session_state.page = 'result'
