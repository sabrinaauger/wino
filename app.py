import streamlit as st

# Declare global variables
global_wine_preference = None
global_flavour_options = None
global_dryness_options = None

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'welcome'

    if st.session_state.page == 'welcome':
        welcome_page()
    elif st.session_state.page == 'survey':
        wine_survey_page()
    elif st.session_state.page == 'result':
        wine_result_page()

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
    if st.button("Get Started"):
        st.session_state.page = 'survey'

def wine_survey_page():
    global global_wine_preference
    global global_flavour_options
    global global_dryness_options

    st.title("Wine Survey")

    # Wine preference section
    st.header("Wine Preference")
    wine_preference = st.radio("Select your wine preference:", ['White', 'Red'])

    # Flavor options section
    st.header("Flavor Options")
    flavour_options = st.multiselect("Select your preferred flavor options:", ['Fruity', 'Floral', 'Herbal', 'Earthy'])

    # Dryness options section
    st.header("Dryness Options")
    dryness_options = st.multiselect("Select your preferred dryness options:", ['Sweet', 'Off-Dry', 'Medium Dry', 'Dry'])

    # Submit button
    if st.button("Submit"):
        st.session_state.page = 'result'
        set_global_variables(wine_preference, flavour_options, dryness_options)

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
    if st.button("I'm not satisfied. Redo the survey"):
        st.warning("Survey reset. Please submit your preferences again.")
        main()

if __name__ == "__main__":
    main()
