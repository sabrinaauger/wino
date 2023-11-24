import streamlit as st
from interface.functions import set_page_to_survey, set_page_to_welcome, suggest_wines
from interface.survey import wine_survey_page
#Set Welcome Page
def welcome_page():
    st.title("Welcome to Wino!")
    st.write("""
        Welcome to our Wine Recommender app! This app helps you discover new wines
        based on your taste preferences.

        **Here's what you can expect:**
        - Answer a few questions about your wine preferences.
        - Get a personalized wine recommendation based on your choices.
        - Discover new wines that match your taste!
    """)
    #Click on button to set page to survey which sends user to survey page
    st.button("Get Started", on_click=set_page_to_survey)

# Define the survey page
def survey_page():
    wine_survey_page()


def wine_result_page():
    # Suggested wines based on preferences
    suggestions = suggest_wines()

    # Display the first suggestion
    st.subheader("Suggested Wine 1:")
    st.write(suggestions[0])

    # Button to show additional suggestions
    if st.button("Show additional suggestions"):
        # Display the second suggestion
        st.subheader("Suggested Wine 2:")
        st.write(suggestions[1])

        # Display the third suggestion
        st.subheader("Suggested Wine 3:")
        st.write(suggestions[2])

    # Redo survey button
    st.button("I'm not satisfied. Redo the survey", on_click=set_page_to_welcome)
