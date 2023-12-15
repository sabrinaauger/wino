import streamlit as st
from interface.data import load_data, load_country
from interface.model import get_recommendations  # Import the recommendation function

# Static variable(s) used in this file
DF = load_data()

# Set page to survey
def set_page_to_survey():
    st.session_state.page = 'survey'

# Set page to welcome
def set_page_to_welcome():
    st.session_state.page = 'welcome'

# Store the variables in our global variables to be used across the pages
def set_global_variables(price_range, wine_preference, selected_country, aroma_options, sweet_option, occasion):
    st.session_state.global_price_range = price_range
    st.session_state.global_wine_preference = wine_preference
    st.session_state.global_country = selected_country
    st.session_state.global_aroma_options = aroma_options
    st.session_state.global_sweet_option = sweet_option
    st.session_state.global_occasion = occasion

# Region selector function
def country_selector():
    # Load data then get the country column from df
    df = load_country(DF)

    # Extract unique countries and sort them alphabetically
    df.sort()
    # Move 'I don't know' to the beginning of the list before 'Canada'
    if "I don't know" in df:
        df.remove("I don't know")
        df.insert(0, "I don't know")

    # Move 'Canada' and 'USA' to the beginning of the list
    if 'Canada' in df:
        df.remove('Canada')
        df.insert(1, 'Canada')

    if 'US' in df:
        df.remove('US')
        df.insert(2, 'US')


    # Display a region selector widget using Streamlit
    selected_country = st.selectbox("Select your preferred country:", df)
    return selected_country

# Occasion selector
def occasion_selector():
    occasion_options = ['No occasion','Anniversary', 'Birthday', 'Summer Pool party', 'Professional diner', 'Brunch',
                        'Seafood restaurant', 'Steakhouse restaurant','Date','To bring to a Dinner Party']
    selected_occasion = st.selectbox("Select the occasion:", occasion_options)
    return selected_occasion

# Once the survey has been submitted...
def submit_survey(price_range, wine_preference, selected_country, aroma_options, sweet_option, selected_occasion):
    set_global_variables(price_range, wine_preference, selected_country, aroma_options, sweet_option, selected_occasion)
    user_input = {
        'wine_type': wine_preference,
        'preproc_description': ', '.join(aroma_options),
        'country': selected_country,
        'dry_sweet': sweet_option,
        'aroma': aroma_options[0],
        'price': price_range,  # Store price range as a tuple
        'occasion': selected_occasion
    }
    st.session_state.user_input = user_input
    st.session_state.page = 'result'

# Function to suggest wines
def suggest_wines():
    if 'user_input' in st.session_state and st.session_state.user_input is not None:
        user_input = st.session_state.user_input
        recommendations = get_recommendations(user_input)
        return recommendations


# Define the show additional suggestions button function with an initial state
def suggest_button():
    if 'show_additional_suggestions' not in st.session_state:
        st.session_state.show_additional_suggestions = False  # Initialize show_additional_suggestions

    label = "Hide additional suggestions" if st.session_state.show_additional_suggestions else "Show additional suggestions"
    return st.button(label, key="additional_suggestions_button", on_click=suggest_set)

# Function to toggle the state of additional suggestions
def suggest_set():
    st.session_state.show_additional_suggestions = not st.session_state.show_additional_suggestions
    return st.session_state.show_additional_suggestions

# Define the redo survey button
def redo_survey():
    # Clear session state or any other relevant variables
    st.session_state.clear()  # Clear the session state
    set_page_to_survey()  # Redirect to the survey page
