from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.preprocessing import LabelEncoder
from interface.data import load_data
import pandas as pd
from interface.model import get_recommendations



# Example user input
user_input = {'wine_type': 'Red', 'preproc_description': 'fruity and smooth', 'country': 'France', 'dry_sweet': 'Dry', 'aroma': 'Fruity', 'price': 30}

# Get recommendations
recommendations = get_recommendations(user_input)
print(recommendations[['country', 'description', 'points', 'price', 'title', 'wine_type', 'dry_sweet', 'aroma']])
