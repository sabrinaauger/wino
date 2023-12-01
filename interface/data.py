# Necessary imports
import pandas as pd
import streamlit as st

#Function to load the main dataset used
@st.cache_data
def load_data():
    dataset_path = '~/code/sabrinaauger/wino/data/clean_data/wine_reviews.csv'
    wine_df = pd.read_csv(dataset_path)
    return wine_df

#Creating function that loads the type of wine from a wine dataset
def load_type(df):
    type_column = df['wine_type']
    return type_column

# Creating function that loads the country from a wine dataset
def load_country(df):
    # Load your dataset (adjust the path and format accordingly)
    country_column = df['country']
    return country_column

#Creating function to load price from wine dataset
def load_price(df):
    price_column = df['price']
    return price_column

# Creating function that loads the designation from a wine dataset
def load_designation(df):
    variety_column = df['variety']
    return variety_column

# Creating function to return the minimum and the maximum price value of the wine dataset
def load_price_minmax(df):
    # Get the minimum and maximum prices available on the dataset
    min_price = df['price'].min()
    max_price = df['price'].max()
    return min_price, max_price
