# Necessary imports
import pandas as pd

dataset_path = '~/code/sabrinaauger/wino/interface/wine_reviews.csv'
wine_df = pd.read_csv(dataset_path)

# Creating function that loads the country from a wine dataset
def load_country():
    # Load your dataset (adjust the path and format accordingly)
    country_column = wine_df['country']
    return country_column

#Creating function to load price from wine dataset
def load_price():
    price_column = wine_df['price']

    # Get the minimum and maximum prices available on the dataset
    min_price = price_column.min()
    max_price = price_column.max()

    return price_column, min_price, max_price


# Creating function that loads the variety from a wine dataset
def load_variety():
    variety_column = wine_df['variety']
    return variety_column
