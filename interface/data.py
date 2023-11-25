# Necessary imports
import pandas as pd

# Creating function that loads the country from a wine dataset
def load_country():
    # Load your dataset (adjust the path and format accordingly)
    dataset_path = '~/code/sabrinaauger/wino/raw_data/winemag-data_first150k.csv'
    wine_df = pd.read_csv(dataset_path)
    country_column = wine_df['country']
    return country_column

# Creating function that loads the price from a wine dataset
def load_price():
    dataset_path = '~/code/sabrinaauger/wino/raw_data/winemag-data_first150k.csv'
    wine_df = pd.read_csv(dataset_path)
    price_column = wine_df['price']
    return price_column

# Creating function that loads the variety from a wine dataset
def load_variety():
    dataset_path = '~/code/sabrinaauger/wino/raw_data/winemag-data_first150k.csv'
    wine_df = pd.read_csv(dataset_path)
    variety_column = wine_df['variety']
    return variety_column
