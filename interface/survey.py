import streamlit as st
from interface.functions import submit_survey, country_selector, occasion_selector
from interface.data import load_data, load_price_minmax
from interface.model import get_recommendations

# Load dataset from cache
@st.cache_data
def load_survey_data():
    return load_data()

def wine_survey_page():
    def display_logo():
        st.image('/Users/sabrinaauger/code/sabrinaauger/wino/data/photo/logo.jpeg', width=170)

    # Load the data
    df = load_survey_data()

    display_logo()

    st.title("What kind of wine would you like to try?")

    gif_url = "https://cdn.dribbble.com/users/43342/screenshots/1086690/media/6943db96c8ea7f3dea2314238e1a7fbd.gif"
    st.image(gif_url, caption="There's so many choices! Which one do I choose?", use_column_width=True)

    st.header("Price Range")
    price_ranges = [
        "Under $20",
        "$20 - $50",
        "$50 - $100",
        "$100 - $500",
        "Over $500",
    ]
    selected_price_range = st.selectbox("Select your preferred price range:", price_ranges)
    price_mapping = {
        "Under $20": (4, 20),
        "$20 - $50": (21, 50),
        "$50 - $100": (51, 100),
        "$100 - $500": (101, 500),
        "Over $500": (501, 3300)  # Update upper limit according to your dataset
    }
    price_range = price_mapping[selected_price_range]

    st.header("Wine Preference")
    wine_preference = st.radio("Select your wine preference:", ['White', 'Red', 'Rosé', 'Sparkling', "I don't know"])
    st.session_state.wine_preference = wine_preference

    st.header("Country Selector")
    selected_country = country_selector()
    st.write(f"Selected Country: {selected_country}")
    st.session_state.selected_country = selected_country

    st.header("Flavor Options")
    aroma_options = st.multiselect("Select your preferred flavor options:", ['Fruity', 'Floral', 'Herbal', 'Earthy'])
    if len(aroma_options) == 0:
        st.error("Please choose a flavor to get a wine recommendation.")
    else:
        st.session_state.aroma_options = aroma_options

    st.header("Dryness/Sweetness preference")
    sweet_option = st.radio("Select your preferred dryness/sweetness:", ['Dry', 'Sweet', "I don't know"])
    st.session_state.sweet_option = sweet_option

    st.header("Occasion Selector")
    selected_occasion = occasion_selector()
    st.write(f"Selected Occasion: {selected_occasion}")
    st.session_state.selected_occasion = selected_occasion

    # Submit button
    submit_button_key = "submit_button_key"
    if st.button("Submit", key=submit_button_key):
        # Store user input in session state with also the occasion
        user_input = {
            'wine_type': wine_preference,
            'preproc_description': ', '.join(aroma_options),
            'country': selected_country,
            'dry_sweet': sweet_option,
            'aroma': aroma_options[0],
            'price': price_range,  # Ensure price_range is a tuple of (min_price, max_price)
            'occasion':selected_occasion
        }
        st.session_state.user_input = user_input
        submit_survey(price_range, wine_preference, selected_country, aroma_options, sweet_option,selected_occasion)
