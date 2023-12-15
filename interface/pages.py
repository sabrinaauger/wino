import streamlit as st
from interface.functions import set_page_to_survey, suggest_wines, suggest_button, redo_survey
from interface.survey import wine_survey_page
from interface.data import load_data


# Function to display the logo in the header
def display_logo_in_header():
    header = st.columns([4, 1])  # Adjust column widths
    with header[0]:
        # First logo on the left-hand side
        st.image('data/photo/logo.jpeg', width=170)

    with header[1]:
        # Second logo on the right-hand side (smaller for le wagon logo)
        st.image('data/photo/logowagon2.png', width=50)  # Adjust the width to make it smaller

    return st


#Function to ensure that the page loaded displays the top of the page
def welcome_page():

    # Logo and title layout for welcome page
    header_st = display_logo_in_header()
    # Full-width image before "Welcome to Wino!" title
    st.image('data/photo/image5.jpeg', caption="Life is too short to drink bad wine. So wine a bit, you'll feel better!", use_column_width=True)

    # Welcome message in a designed layout within the body
    st.markdown(
        """
        <div style='padding: 20px; border-radius: 10px;'>
            <h1 style='text-align: center; color: #2f4f4f;'>Welcome to Wino!</h1>
            <p style='text-align: justify; color: #2f4f4f;'>
                Welcome to Wino, our Wine Recommender app! This app helps you discover new wines based on your taste preferences.
            </p>
            <h3 style='text-align: left; color: #2f4f4f;'>Here's what you can expect:</h3>
            <ul style='text-align: left; color: #2f4f4f;'>
                <li>Answer a few questions about your wine preferences.</li>
                <li>Get a personalized wine recommendation based on your choices.</li>
                <li>Discover new wines that match your taste!</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Click on button to set page to survey which sends the user to the survey page
    st.button("Get Started", on_click=set_page_to_survey, key="get_started_button")

# Load data
df = load_data()

# Define welcome_page function
# def welcome_page():

#    scroll_to_top() # No need to redefine, as it's already defined above

# Define survey page
def survey_page():
    wine_survey_page()

# Define result page
def wine_result_page():
    header_st = display_logo_in_header()

    # Call scroll_to_top function to ensure automatic scrolling to the top
    #scroll_to_top()

    if 'user_input' not in st.session_state:
        st.error("Please fill out the survey first.")
        return

    user_input = st.session_state.user_input

    # Get wine suggestions using user_input
    recommendations = suggest_wines()

    # Returnong message and allowing the user to redo_survey if no reco
    if recommendations is None or recommendations.empty:
        st.warning("No wine recommendations found based on your preferences. Please retry the survey.")
        st.button("Redo Survey", on_click=redo_survey)
        st.markdown(
            "<p style='text-align: center; font-size: 18px; color: #2f4f4f;'>Cheers!</p>",
            unsafe_allow_html=True
        )
        return
    # Add gif
    gif_url = "https://media1.tenor.com/m/fd6I3YkDAZoAAAAC/cheers-are-you-the-one.gif"
    # Display the GIF at the end
    st.image(gif_url, use_column_width=True)
    # Separator for better section division
    st.markdown("---")

    # Display "Suggested Wines:" at the top
    st.markdown("<h3 style='text-align: left; color: #2f4f4f;'>Suggested Wines:</h3>", unsafe_allow_html=True)

    # Check if there are any recommendations
    if recommendations is None or recommendations.empty:
        st.warning("No wine recommendations found based on your preferences. Please retry the survey.")
        st.button("Redo Survey", on_click=redo_survey)
        st.markdown(
        "<p style='text-align: center; font-size: 18px; color: #2f4f4f;'>Cheers!</p>",
        unsafe_allow_html=True
    )
    else:
        # Display the first wine recommendation
        first_recommendation = recommendations.iloc[0]
        st.markdown(
            f"**Wine title:** {first_recommendation['title']} <br>"
            f"**Wine Variety:** {first_recommendation['wine_variety']} <br>"
            f"**Price:** ${first_recommendation['price']} <br>"
            f"**Description:** {first_recommendation['description']} <br>"
            f"**Country:** {first_recommendation['country']}",
            unsafe_allow_html=True
        )

    # Create a checkbox to act as the button
    show_additional_suggestions = st.checkbox("Show additional suggestions")

    # Check if the checkbox is checked
    if show_additional_suggestions:
        additional_recommendations = suggest_wines()

        # Display additional suggestions using additional_recommendations
        seen_titles = set([first_recommendation['title']])
        count = 0  # Counter to limit the number of displayed suggestions
        for index, recommendation in additional_recommendations.iterrows():
            if recommendation['title'] not in seen_titles and count < 3:
                seen_titles.add(recommendation['title'])
                st.markdown(
                    f"**Wine title:** {recommendation['title']} <br>"
                    f"**Wine Variety:** {recommendation['wine_variety']} <br>"
                    f"**Price:** ${recommendation['price']} <br>"
                    f"**Description:** {recommendation['description']} <br>"
                    f"**Country:** {recommendation['country']}",
                    unsafe_allow_html=True
                )
                count += 1

    # Add a button to give the chance to the user to redo the survey if they want
    st.button("Redo Survey", on_click=redo_survey)

    # Add "Cheers!" with similar style as st.image() caption
    st.markdown(
        "<p style='text-align: center; font-size: 18px; color: #2f4f4f;'>Cheers!</p>",
        unsafe_allow_html=True
    )
