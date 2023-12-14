# Necessary imports
import pandas as pd
# import streamlit as st
# import pickle
# import gdown
# import os

# #Function to download the dataset from Google Drive
# @st.cache_data
# def gdown_download():
#     url = "https://docs.google.com/spreadsheets/d/1CIGRbJD9IM_LEgXOwKL8jsHkFSdSXkqc/"  # change link ID
#     file_id = url.split('/')[-2]
#     prefix = 'https://drive.google.com/uc?/export=download&id='
#     excel_file = "dataset1.xlsx"

#     # Check if the file already exists
#     if os.path.exists(excel_file):
#         print(f"The file '{excel_file}' already exists. Skipping download.")
#     else:
#         # Download the file
#         gdown.download(prefix + file_id, excel_file)
#         print(f"The file '{excel_file}' has been downloaded successfully.")

# Function to load the main dataset used
def load_data():
    csv_path = "/Users/sabrinaauger/code/sabrinaauger/wino/data/cleaned_data/wine_reviews_df.csv"  # Replace with the actual path to your CSV file
    # csv_path ='https://raw.githubusercontent.com/sabrinaauger/wino/master/data/cleaned_data/wine_reviews_df.csv'
    data_load = pd.read_csv(csv_path)

    # Convert 'price' column to numeric type
    data_load['price'] = pd.to_numeric(data_load['price'], errors='coerce')  # Assuming 'price' column contains numeric values

    # Clean up 'wine_variety' and 'title' columns
    data_load['wine_variety'] = data_load['wine_variety'].str.replace('Rosee', 'Rose')
    data_load['title'] = data_load['title'].str.replace('Rosee', 'Rose')

    return data_load

def load_chunkdata(chunk_size):
    csv_path = "/Users/sabrinaauger/code/sabrinaauger/wino/data/cleaned_data/wine_reviews_df.csv"
    # Replace with the actual path to github repository
    #csv_path ='https://raw.githubusercontent.com/sabrinaauger/wino/master/data/cleaned_data/wine_reviews_df.csv'
    data_loader = pd.read_csv(csv_path, chunksize=chunk_size)
    return data_loader

#If model is implemented, may not need these functions
#Creating function that loads the type of wine from a wine dataset
def load_type(df):
    type_column = df['wine_type']
    type_column.append("I don't know")
    return type_column

# Creating function that loads the country from a wine dataset
def load_country(df):
    # Load your dataset
    country_column = df['country'].unique().tolist()
    country_column.append("I don't know")
    return country_column


#Creating function to load price from wine dataset
def load_price(df):
    price_column = df['price']
    return price_column

# #Creating function to load the dry/sweet variable from wine dataset
def load_sweet(df):
    sweet_column = df['dry_sweet']
    sweet_column.append("I don't know")
    return sweet_column

# # Creating function to load the aroma variable from wine dataset
def load_aroma(df):
    aroma_column = df['aroma']
    return aroma_column

# # Creating function to return the minimum and the maximum price value of the wine dataset
def load_price_minmax(df):
    min_price = df['price'].min()
    max_price = df['price'].max()
    return min_price, max_price
