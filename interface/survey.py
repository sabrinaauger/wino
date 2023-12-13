import streamlit as st
from interface.functions import submit_survey, country_selector
from interface.data import load_data, load_price_minmax
# from interface.model import get_recommendations

# Load dataset from cache
@st.cache_data
def load_survey_data():
    return load_data()

def wine_survey_page():
   #Display the logo wino - the path should be changed to github path
    def display_logo():
        st.image('data/photo/logo.jpeg', width=170)

    #Load the data
    df = load_survey_data()

    display_logo()

    st.title("What kind of wine would you like to try?")

    # Test gif for the survey page
    gif_url = "https://cdn.dribbble.com/users/43342/screenshots/1086690/media/6943db96c8ea7f3dea2314238e1a7fbd.gif"
    st.image(gif_url, caption="There's so many choices! Which one do I choose?", use_column_width=True)

    # Price range selector
    st.header("Price Range")
    # Load price minimum and maximum values
    price_min, price_max = load_price_minmax(df)
    # Define predefined price range options
    price_ranges = [
        "Under $20",
        "$20 - $50",
        "$50 - $100",
        "$100 - $500",
        "Over $500",
    ]
    # Display dropdown to select price range
    selected_price_range = st.selectbox("Select your preferred price range:", price_ranges)
    # Map selected price range to corresponding values
    price_mapping = {
        "Under $20": (4, 20),
        "$20 - $50": (21, 50),
        "$50 - $100": (51, 100),
        "$100 - $500": (101,500),
        "Over $500": (501, 3300)  # Update upper limit according to your dataset
    }
    # Set price range based on selected option
    price_range = price_mapping[selected_price_range]

    # Wine preference section
    st.header("Wine Preference")
    wine_preference = st.radio("Select your wine preference:", ['White', 'Red', 'Rosé', 'Sparkling'])
    st.session_state.wine_preference = wine_preference

    # Country selection
    st.header("Country Selector")
    selected_country = country_selector()
    st.write(f"Selected Country: {selected_country}")
    st.session_state.selected_country = selected_country

    # Flavor options section
    st.header("Flavor Options")
    aroma_options = st.multiselect("Select your preferred flavor options:", ['Fruity', 'Floral', 'Herbal', 'Earthy'])
    st.session_state.aroma_options = aroma_options

    # Dryness/Sweetness options section
    st.header("Dryness/Sweetness preference")
    sweet_option = st.radio("Select your preferred dryness/sweetness:", ['Dry', 'Sweet'])
    st.session_state.sweet_option = sweet_option

    # Submit button
    submit_button_key = "submit_button_key"
    if st.button("Submit", key=submit_button_key):
        # Store user input in session state
        user_input = {
            'wine_type': wine_preference,
            'preproc_description': ', '.join(aroma_options),
            'country': selected_country,
            'dry_sweet': sweet_option,
            'aroma': aroma_options[0],
            'price': price_range  # Ensure price_range is a tuple of (min_price, max_price)
        }
        st.session_state.user_input = user_input
        submit_survey(
            st.session_state.user_input['price'],
            st.session_state.user_input['wine_type'],
            st.session_state.user_input['country'],
            st.session_state.user_input['aroma'],
            st.session_state.user_input['dry_sweet']
        )
