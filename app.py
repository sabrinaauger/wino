import streamlit as st

def main():
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
        st.success("Survey submitted successfully!")
        display_survey_results(wine_preference, flavour_options, dryness_options)

def display_survey_results(wine_preference, flavour_options, dryness_options):
    st.subheader("Survey Results")
    st.write(f"Wine Preference: {wine_preference}")
    st.write(f"Flavor Options: {', '.join(flavour_options)}")
    st.write(f"Dryness Options: {', '.join(dryness_options)}")

    # Suggested wine based on preferences
    suggested_wine = suggest_wine(wine_preference, flavour_options, dryness_options)
    st.subheader("Suggested Wine:")
    st.write(suggested_wine)

    # Button to request another suggestion
    if st.button("I do not like this one, show me another similar one"):
        st.warning("Here's another suggestion:")
        new_suggestion = suggest_wine(wine_preference, flavour_options, dryness_options)
        st.write(new_suggestion)

def suggest_wine(wine_preference, flavour_options, dryness_options):
    # Replace this with your logic to suggest a wine based on preferences
    # You can use external APIs, databases, or any other method to fetch wine suggestions.
    # For simplicity, a placeholder suggestion is used here.
    return f"A recommended wine for your preferences: {wine_preference} with {', '.join(flavour_options)} flavors and {', '.join(dryness_options)} dryness."

if __name__ == "__main__":
    main()
