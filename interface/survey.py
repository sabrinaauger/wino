# survey.py

import streamlit as st
from interface.functions import submit_survey
from interface.data import load_region

def wine_survey_page():
    # Declare global variables that will be used
    global global_price_range
    global global_wine_preference
    global global_region
    global global_flavour_options
    global global_dryness_options

    # Region selector function
    def region_selector():
        # Use the load_region function from data.py
        wine_regions_df = load_region()

        # Display a region selector widget using Streamlit
        selected_region = st.selectbox("Select your preferred region:", wine_regions_df['region_1'].unique())
        return selected_region

    st.title("Wine Survey")

    # Price range selector
    st.header("Price Range")
    price_range = st.slider("Select your preferred price range:", min_value=0, max_value=100, value=(10, 50), step=1)

    # Wine preference section
    st.header("Wine Preference")
    wine_preference = st.radio("Select your wine preference:", ['White', 'Red'])

    #Region selection
    st.header("Region Selector")
    selected_region = region_selector()
    st.write(f"Selected Region: {selected_region}")

    # Flavor options section
    st.header("Flavor Options")
    flavour_options = st.multiselect("Select your preferred flavor options:", ['Fruity', 'Floral', 'Herbal', 'Earthy'])

    # Dryness options section
    st.header("Dryness Options")
    dryness_options = st.multiselect("Select your preferred dryness options:", ['Sweet', 'Off-Dry', 'Medium Dry', 'Dry'])

    # Submit button
    st.button("Submit", on_click=lambda: submit_survey(price_range, wine_preference, selected_region, flavour_options, dryness_options))
