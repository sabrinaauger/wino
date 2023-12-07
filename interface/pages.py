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

    cat_gif = "https://media.tenor.com/oiW1k6gAvNwAAAAd/cat-red-wine.gif"
    st.image(cat_gif, caption="Sometimes, it's best to just enjoy the moment... with some drinks 🙃", use_column_width=True)
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
        description, recommendations, country_chosen, variety, aroma_chosen, prices = suggest_wines()

        # Display the suggestions
        st.header(f"Suggested {aroma_chosen} Wines from {country_chosen}:")
        if recommendations[0] == "N/A":
            st.write("No available options.")
        elif recommendations[0] != "N/A":
            # Display the first suggestion, price, and description
            st.write(len(recommendations))

            st.subheader("Suggested Wine 1:")
            st.write(f"Recommendation: {recommendations[0]}")
            st.write(f"Variety: {variety[0]}")
            st.write(f"Price: ${prices[0]}")
            st.write(f"{description[0]}")
            drunk_gif = "https://media.tenor.com/Q399o5To0UsAAAAj/queondapa.gif"
            st.image(drunk_gif, caption="We got something!", use_column_width=True)
           # Check if there are additional suggestions to show
        if len(recommendations) > 1:
        # Button to show additional suggestions
            if suggest_button():
                # Display the second suggestion, price, and description
                st.subheader("Suggested Wine 2:")
                st.write(f"Recommendation: {recommendations[1]}")
                st.write(f"Variety: {variety[1]}")
                st.write(f"Price: ${prices[1]}")
                st.write(f"{description[1]}")

                # Display the third suggestion, price, and description
                st.subheader("Suggested Wine 3:")
                st.write(f"Recommendation: {recommendations[2]}")
                st.write(f"Variety: {variety[2]}")
                st.write(f"Price: ${prices[2]}")
                st.write(f"{description[2]}")

                drunker_gif = "https://media.tenor.com/FR32Y0FB6RgAAAAC/bruh-moment-fall.gif"
                st.image(drunker_gif, caption="We got even more!", use_column_width=True)
                # Hide the "Show additional suggestions" button after clicking
                st.session_state.show_additional_suggestions = False
        else:
            st.subheader("No other suggestions available. Please retry with different settings for more suggestions. 🍷")
            emote_url = "https://i.kym-cdn.com/photos/images/original/000/325/934/060.png"
            st.image(emote_url, caption="You could've done better in your choices.", use_column_width=True)
    # Redo survey button
    redo_survey()
