# survey.py

import streamlit as st
from interface.functions import submit_survey
from interface.data import load_country

def wine_survey_page():
    # Declare global variables that will be used
    global global_price_range
    global global_wine_preference
    global global_country
    global global_flavour_options
    global global_dryness_options

    # Region selector function
    def country_selector():
        # Use the load_country function from data.py
        df = load_country()

        # Display a region selector widget using Streamlit
        selected_country = st.selectbox("Select your preferred region:", df.unique())
        return selected_country

    st.title("Wine Survey")

    # Price range selector
    st.header("Price Range")
    price_range = st.slider("Select your preferred price range:", min_value=0, max_value=100, value=(10, 50), step=1)

    # Wine preference section
    st.header("Wine Preference")
    wine_preference = st.radio("Select your wine preference:", ['White', 'Red'])

    #Country selection
    st.header("Country Selector")
    selected_country = country_selector()
    st.write(f"Selected Country: {selected_country}")

    # Flavor options section
    st.header("Flavor Options")
    flavour_options = st.multiselect("Select your preferred flavor options:", ['Fruity', 'Floral', 'Herbal', 'Earthy'])

    # Dryness options section
    st.header("Dryness Options")
    dryness_options = st.multiselect("Select your preferred dryness options:", ['Sweet', 'Off-Dry', 'Medium Dry', 'Dry'])

    # Submit button
    st.button("Submit", on_click=lambda: submit_survey(price_range, wine_preference, selected_country, flavour_options, dryness_options))
