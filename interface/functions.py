# Many imports for functions for other pages, but also a few for similar semantics for tokens
import streamlit as st
from interface.data import (
    load_data, load_type, load_country, load_price, load_sweet, load_aroma
)

#Set page to survey
def set_page_to_survey():
    st.session_state.page = 'survey'
#set page to welcome
def set_page_to_welcome():
    st.session_state.page = 'welcome'

#store the variables in our global variables to be used across the pages
def set_global_variables(price_range, wine_preference, selected_country, aroma_options, sweet_option):
    global global_price_range
    global global_wine_preference
    global global_country
    global global_aroma_options
    global global_sweet_option

    global_price_range = price_range
    global_wine_preference = wine_preference
    global_country = selected_country
    global_aroma_options = aroma_options
    global_sweet_option = sweet_option

# Region selector function
def country_selector():
    # Load data then get the country column from df
    df = load_country(load_data())

    # Extract unique countries and sort them alphabetically
    unique_countries = df.unique().tolist()
    unique_countries.sort()

    # Move 'Canada' and 'USA' to the beginning of the list
    if 'Canada' in unique_countries:
        unique_countries.remove('Canada')
        unique_countries.insert(0, 'Canada')

    if 'USA' in unique_countries:
        unique_countries.remove('USA')
        unique_countries.insert(1, 'USA')

    # Display a region selector widget using Streamlit
    selected_country = st.selectbox("Select your preferred country:", unique_countries)
    return selected_country

# This is base suggest_wines() with price and country only
def suggest_wines():
    # Access variables from the global scope
    price_range = global_price_range
    wine_preference = global_wine_preference
    selected_country = global_country
    aroma_options = global_aroma_options
    sweet_option = global_sweet_option

    # Loading dataset as needed to find the right suggestion
    df = load_data()
    wine_price= load_price(df)

    # Filter the main dataset with the given input the user has given
    suggestion_df = df[
        (load_country(df) == selected_country) &
        (wine_price >= price_range[0]) &
        (wine_price <= price_range[1]) &
        (load_sweet(df) == sweet_option) &
        (load_aroma(df).isin(aroma_options)) &
        (load_type(df) == wine_preference)
    ]

    # Ensure there are at least 3 suggestions
    if not suggestion_df.empty:
        # Sort the dataset based on 'points' in descending order
        suggestion_df = suggestion_df.sort_values(by='points', ascending=False)

        # Deduplicate based on 'title'
        suggestion_df = suggestion_df.drop_duplicates(subset='title')

        # Extract unique titles
        unique_recommendations_titles = suggestion_df['title'].unique()[:3]

        # Filter the dataset based on unique titles
        unique_recommendations_data = suggestion_df[suggestion_df['title'].isin(unique_recommendations_titles)]

        # Extracting specific information for each recommendation
        recommendations = unique_recommendations_data['title'].tolist()
        variety = unique_recommendations_data['wine_variety'].tolist()
        description = unique_recommendations_data['description'].tolist()
        prices = unique_recommendations_data['price'].tolist()
        aroma_chosen = aroma_options
        country_chosen = selected_country


    else:
        # If no wines match the criteria, provide a generic suggestion for each element
        recommendations = ["N/A"]
        variety = ["N/A"]
        description = ["N/A"]
        prices = ["N/A"]
        aroma_chosen = aroma_options
        country_chosen = selected_country

    return description, recommendations, country_chosen, variety, aroma_chosen, prices

#Once the survey has been submitted...
def submit_survey(price_range, wine_preference, selected_country, aroma_options, sweet_option):
    #...we store the variables in our global variables to be used across the pages
    set_global_variables(price_range,wine_preference, selected_country, aroma_options, sweet_option)
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
