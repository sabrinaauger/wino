import streamlit as st

#Set page to survey
def set_page_to_survey():
    st.session_state.page = 'survey'

def set_page_to_welcome():
    st.session_state.page = 'welcome'

#store the variables in our global variables to be used across the pages
def set_global_variables(wine_preference, flavour_options, dryness_options):
    global global_wine_preference
    global global_flavour_options
    global global_dryness_options

    global_wine_preference = wine_preference
    global_flavour_options = flavour_options
    global_dryness_options = dryness_options

def suggest_wines():
    # Access variables from the global scope
    wine_preference = global_wine_preference
    flavour_options = global_flavour_options
    dryness_options = global_dryness_options

    # Replace this with your logic to suggest wines based on preferences
    # For simplicity, placeholder suggestions are used here.
    suggestion_parts = [f"A recommended wine for your preferences: {wine_preference}"]

    if flavour_options:
        suggestion_parts.append(f"with {', '.join(flavour_options)} flavors")

    if dryness_options:
        suggestion_parts.append(f"and {', '.join(dryness_options)} dryness")

    suggestion1 = ' '.join(suggestion_parts) + "."
    suggestion2 = "Another suggestion based on your preferences..."
    suggestion3 = "Yet another suggestion based on your preferences..."

    return [suggestion1, suggestion2, suggestion3]

#Once the survey has been submitted...
def submit_survey(wine_preference, flavour_options, dryness_options):
    #...we store the variables in our global variables to be used across the pages
    set_global_variables(wine_preference, flavour_options, dryness_options)
    #set to result to go to result page
    st.session_state.page = 'result'
