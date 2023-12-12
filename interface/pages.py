import streamlit as st
from interface.functions import set_page_to_survey, suggest_wines, suggest_button, redo_survey
from interface.survey import wine_survey_page
from interface.data import load_data


# Function to display the logo in the header
def display_logo_in_header():
    header = st.columns([4, 1])  # Adjust column widths
    with header[0]:
        # First logo on the left-hand side
        st.image('/Users/sabrinaauger/code/sabrinaauger/wino/data/photo/logo.jpeg', width=170)

    with header[1]:
        # Second logo on the right-hand side (smaller for le wagon logo)
        st.image('/Users/sabrinaauger/code/sabrinaauger/wino/data/photo/logowagon2.png', width=50)  # Adjust the width to make it smaller

    return st


#Function to ensure that the page loaded displays the top of the page
def scroll_to_top():
    # Create an anchor at the top of the page
    st.markdown("<div id='top'></div>", unsafe_allow_html=True)

    # JavaScript to scroll to the top of the page
    st.markdown(
        """
        <script>
        // Function to scroll to the top smoothly
        function scrollToTop() {
            const top = document.getElementById('top');
            top.scrollIntoView({ behavior: 'smooth' });
        }

        // Check condition and scroll to top when satisfied
        if (window.location.hash === '#scrollToTop') {
            scrollToTop();
        }
        </script>
        """,
        unsafe_allow_html=True
    )

# Logo and title layout for welcome page
header_st = display_logo_in_header()
# Full-width image before "Welcome to Wino!" title
st.image('/Users/sabrinaauger/code/sabrinaauger/wino/data/photo/image5.jpeg', caption="Life is too short to drink bad wine. So wine a bit, you'll feel better!", use_column_width=True)

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
def welcome_page():
    scroll_to_top() # No need to redefine, as it's already defined above

# Define survey page
def survey_page():
    wine_survey_page()

# Define result page
# Define result page
# Define result page
def wine_result_page():
    header_st = display_logo_in_header()

     # Call scroll_to_top function to ensure automatic scrolling to the top
    scroll_to_top()

    if 'user_input' in st.session_state:
        recommendations = suggest_wines()

        if recommendations is not None and not recommendations.empty:
            # Stylish header
            st.markdown(
                "<h2 style='text-align: center; color: #2f4f4f;'>It's a Match! Enjoy Your Wine!</h2>",
                unsafe_allow_html=True
            )

            # Display an aesthetic image indicating enjoyment
            enjoyment_image_url = "/Users/sabrinaauger/code/sabrinaauger/wino/data/photo/image2.jpeg"  # Replace this with the URL of your image
            st.image(enjoyment_image_url, use_column_width=True)

            # Separator for better section division
            st.markdown("---")

            # Display "Suggested Wines:" at the top
            st.markdown("<h3 style='text-align: left; color: #2f4f4f;'>Suggested Wines:</h3>", unsafe_allow_html=True)

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

            if st.button("Show additional suggestions"):
                st.markdown("<h4 style='text-align: left; color: #2f4f4f;'>Here are some additional suggestions:</h4>", unsafe_allow_html=True)

                # Retrieve additional suggestions while filtering out those with the same wine title
                seen_titles = set([first_recommendation['title']])
                for index, recommendation in recommendations.iloc[1:5].iterrows():
                    if recommendation['title'] not in seen_titles:
                        seen_titles.add(recommendation['title'])
                        st.markdown(
                            f"**Wine title:** {recommendation['title']} <br>"
                            f"**Wine Variety:** {recommendation['wine_variety']} <br>"
                            f"**Price:** ${recommendation['price']} <br>"
                            f"**Description:** {recommendation['description']} <br>"
                            f"**Country:** {recommendation['country']}",
                            unsafe_allow_html=True
                        )

            # Add a button to give the chance to the user to redo the survey if they want
            if st.button("Redo Survey"):
                if 'additional_suggestions_displayed' in st.session_state:
                    st.session_state.additional_suggestions_displayed = True  # Set the flag to True
                redo_survey()

            # Add "Cheers!" with similar style as st.image() caption
            st.markdown(
                "<p style='text-align: center; font-size: 18px; color: #2f4f4f;'>Cheers!</p>",
                unsafe_allow_html=True
            )
            # Add gif
            #gif_url = "https://media1.tenor.com/m/fd6I3YkDAZoAAAAC/cheers-are-you-the-one.gif"
            # Display the GIF at the end
            #st.image(gif_url, use_column_width=True)
        else:
            st.subheader("No recommendations available. Please retry with different settings for more suggestions. 🍷")
            emote_url = "https://i.kym-cdn.com/photos/images/original/000/325/934/060.png"
            st.image(emote_url, caption="You could've done better in your choices.", use_column_width=True)
            if st.button("Retry with different settings"):
                redo_survey()

        # JavaScript to scroll to the top of the page
        scroll_to_top_js = """
            <script>
            // Wait for the page to load first
            window.onload = function() {
                // Get the top of the page
                const top = document.getElementById('top');
                // Scroll to the top smoothly
                top.scrollIntoView({ behavior: 'smooth' });
            }
            </script>
        """
        st.markdown(scroll_to_top_js, unsafe_allow_html=True)

    else:
        st.error("Please fill out the survey first.")
        redo_survey()

 # Create a placeholder to trigger the automatic scroll
    st.empty()
