# Necessary imports
import pandas as pd
import streamlit as st

#Function to load the main dataset used
@st.cache_data
def load_data():
    dataset_path = '~/code/sabrinaauger/wino/data/clean_data/wine_reviews.csv' #change path to a cloud one
    wine_df = pd.read_csv(dataset_path)
    return wine_df

#Creating function that loads the type of wine from a wine dataset
@st.cache_data
def load_type(df):
    type_column = df['wine_type']
    return type_column

# Creating function that loads the country from a wine dataset
@st.cache_data
def load_country(df):
    # Load your dataset (adjust the path and format accordingly)
    country_column = df['country']
    return country_column

#Creating function to load price from wine dataset
@st.cache_data
def load_price(df):
    price_column = df['price']
    return price_column

#Creating function to load the dry/sweet variable from wine dataset
@st.cache_data
def load_sweet(df):
    sweet_column = df['dry_sweet']
    return sweet_column

# Creating function to load the aroma variable from wine dataset
@st.cache_data
def load_aroma(df):
    aroma_column = df['aroma']
    return aroma_column

# Creating function that loads the designation from a wine dataset
@st.cache_data
def load_designation(df):
    variety_column = df['title']
    return variety_column

# Creating function to return the minimum and the maximum price value of the wine dataset
@st.cache_data
def load_price_minmax(df):
    # Get the minimum and maximum prices available on the dataset
    min_price = df['price'].min()
    max_price = df['price'].max()
    return min_price, max_price
