#variables flavour and dryness are currently placeholders, need to add more options depending on data

import streamlit as st

#Set page to survey
def set_page_to_survey():
    st.session_state.page = 'survey'

def set_page_to_welcome():
    st.session_state.page = 'welcome'

#store the variables in our global variables to be used across the pages
def set_global_variables(price_range, wine_preference, flavour_options, dryness_options):
    global global_price_range
    global global_wine_preference
    global global_flavour_options
    global global_dryness_options

    global_price_range = price_range
    global_wine_preference = wine_preference
    global_flavour_options = flavour_options
    global_dryness_options = dryness_options

def suggest_wines():
    # Access variables from the global scope
    price_range = global_price_range
    wine_preference = global_wine_preference
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
        recommendations.append("Generic Wine Choice")

    return recommendations


#Once the survey has been submitted...
def submit_survey(price_range, wine_preference, flavour_options, dryness_options):
    #...we store the variables in our global variables to be used across the pages
    set_global_variables(price_range,wine_preference, flavour_options, dryness_options)
    #set to result to go to result page
    st.session_state.page = 'result'
