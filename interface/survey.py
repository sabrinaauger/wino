import streamlit as st
from interface.functions import submit_survey, country_selector, set_global_variables
from interface.data import load_data, load_price_minmax

#Load dataset from cache
@st.cache_data
def load_survey_data():
    return load_data()
def wine_survey_page():
    #load data
    df = load_survey_data()

    st.title("Wine Survey")

    # Price range selector
    st.header("Price Range")
    price_min, price_max = load_price_minmax(df)
    price_range = st.slider("Select your preferred price range:", min_value=int(price_min), max_value=int(price_max), value=(10, 50), step=1)

    # Wine preference section
    st.header("Wine Preference")
    wine_preference = st.radio("Select your wine preference:", ['White', 'Red', 'Rosé', 'Sparkling'])

    #Country selection
    st.header("Country Selector")
    selected_country = country_selector()
    st.write(f"Selected Country: {selected_country}")

    # Flavor options section
    st.header("Flavor Options")
    aroma_options = st.multiselect("Select your preferred flavor options:", ['Fruity', 'Floral', 'Herbal', 'Earthy'])

    # Dryness/Sweetness options section
    st.header("Dryness/Sweetness preference")
    sweet_option = st.radio("Select your preferred dryness/sweetness:", ['Dry', 'Sweet'])

    # Submit button
    submit_button_key = "submit_button_key"
    st.button("Submit", key=submit_button_key, on_click=lambda: submit_survey(price_range, wine_preference, selected_country, aroma_options, sweet_option))

    #Test gif for the survey page
    gif_url = "https://cdn.dribbble.com/users/43342/screenshots/1086690/media/6943db96c8ea7f3dea2314238e1a7fbd.gif"
    st.image(gif_url, caption='Image from URL', use_column_width=True)
