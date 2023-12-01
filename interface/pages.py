import streamlit as st
from interface.functions import set_page_to_survey, suggest_wines, suggest_button, redo_survey
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

#Define the result page
def wine_result_page():
    # Add a new flag to session state for controlling visibility
    if 'show_additional_suggestions' not in st.session_state:
        st.session_state.show_additional_suggestions = True  # Set it to True initially to show suggestions

    # Show a loading spinner while the suggestions are being generated
    with st.spinner("Loading recommendations..."):
        # Get wine suggestions
        recommendations, descriptions, prices = suggest_wines()

        # Display the suggestions
        st.header("Suggested Wines:")
        if not recommendations:
            st.write("No available options. Please retry. 🍷")
        else:
            # Display the first suggestion, price, and description
            st.subheader("Suggested Wine 1:")
            st.write(f"Recommendation: {recommendations[0]}")
            st.write(f"Price: ${prices[0]:,.2f}")
            st.write(f"Description: {descriptions[0]}")

           # Check if there are additional suggestions to show
        if len(recommendations) > 1:
        # Button to show additional suggestions
            if suggest_button():
                # Display the second suggestion, price, and description
                st.subheader("Suggested Wine 2:")
                st.write(f"Recommendation: {recommendations[1]}")
                st.write(f"Price: ${prices[1]:,.2f}")
                st.write(f"Description: {descriptions[1]}")

                # Display the third suggestion, price, and description
                st.subheader("Suggested Wine 3:")
                st.write(f"Recommendation: {recommendations[2]}")
                st.write(f"Price: ${prices[2]:,.2f}")
                st.write(f"Description: {descriptions[2]}")

                # Hide the "Show additional suggestions" button after clicking
                st.session_state.show_additional_suggestions = False
        else:
            st.subheader("No other suggestions available. Please retry with different settings for more suggestions. 🍷")

    # Redo survey button
    redo_survey()
