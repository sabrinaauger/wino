import streamlit as st
from pages import welcome_page, survey_page, wine_result_page
# Declare global variables
global_price_range = None
global_wine_preference = None
global_flavour_options = None
global_dryness_options = None

#Define page state
def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'welcome'

    if st.session_state.page == 'welcome':
        welcome_page()
    elif st.session_state.page == 'survey':
        survey_page()
    elif st.session_state.page == 'result':
        wine_result_page()

if __name__ == "__main__":
    main()
