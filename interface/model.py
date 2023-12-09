from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.preprocessing import LabelEncoder
from data import load_data
import pandas as pd

# Assuming 'df' is your DataFrame containing the dataset
# # Load data
data = load_data()
df = pd.DataFrame(data)
# Preprocess categorical variables
label_encoder = LabelEncoder()
df['wine_type'] = label_encoder.fit_transform(df['wine_type'])
df['country'] = label_encoder.fit_transform(df['country'])
df['aroma'] = label_encoder.fit_transform(df['aroma'])
df['dry_sweet'] = label_encoder.fit_transform(df['dry_sweet'])

# Feature engineering for text data
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['preproc_description'])

# Combine numerical and text features
combined_matrix = tfidf_matrix  # You can concatenate other numerical features as well

# Train a similarity-based model
cosine_sim = linear_kernel(combined_matrix, combined_matrix)

# Function to get recommendations based on user input
def get_recommendations(user_input):
    user_input_encoded = label_encoder.transform([user_input['wine_type']])[0]
    # Repeat for other categorical variables in user input

    # Combine user input with existing data
    user_input_matrix = tfidf_vectorizer.transform([user_input['preproc_description']])
    combined_user_matrix = user_input_matrix  # You can concatenate other numerical features as well

    # Calculate cosine similarity between user input and existing data
    similarity_scores = linear_kernel(combined_user_matrix, combined_matrix).flatten()

    # Get indices of top recommendations
    top_indices = similarity_scores.argsort()[:-6:-1]

    # Return recommended items
    return df.iloc[top_indices]

# Example user input
user_input = {'wine_type': 'Red', 'preproc_description': 'fruity and smooth', 'country': 'France', 'dry_sweet': 'Dry', 'aroma': 'Fruity', 'price': 30}

# Get recommendations
recommendations = get_recommendations(user_input)
print(recommendations[['country', 'description', 'points', 'price', 'title', 'wine_type', 'dry_sweet', 'aroma']])
