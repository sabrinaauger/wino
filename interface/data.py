# Necessary imports
import pandas as pd
def load_data():
    dataset_path = '~/code/sabrinaauger/wino/interface/wine_reviews.csv'
    wine_df = pd.read_csv(dataset_path)
    return wine_df

# Creating function that loads the country from a wine dataset
def load_country(df):
    # Load your dataset (adjust the path and format accordingly)
    country_column = df['country']
    return country_column

#Creating function to load price from wine dataset
def load_price(df):
    price_column = df['price']

    # Get the minimum and maximum prices available on the dataset
    min_price = price_column.min()
    max_price = price_column.max()

    return price_column, min_price, max_price

# Creating function that loads the designation from a wine dataset
def load_designation(df):
    variety_column = df['variety']
    return variety_column
