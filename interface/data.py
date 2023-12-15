# Necessary imports
import pandas as pd

# Function to load the main dataset used
def load_data():
    csv_path = "data/cleaned_data/wine_reviews_df.csv"
    data_load = pd.read_csv(csv_path)

    # Clean up 'wine_variety' and 'title' columns
    data_load['wine_variety'] = data_load['wine_variety'].str.replace('Rosee', 'Rose')
    data_load['title'] = data_load['title'].str.replace('Rosee', 'Rose')

    return data_load

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
