from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from interface.data import load_data
import pandas as pd
import pickle
# import streamlit as st

# Load data
data = load_data()
df = pd.DataFrame(data)
#df = df.head(5000)
# Feature engineering for text data
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
tfidf_matrix = tfidf_vectorizer.fit_transform(df['preproc_description'])

# Save the TF-IDF vectorizer and matrix using pickle
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)

with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)

# Function to load the saved TF-IDF vectorizer and matrix
def load_tfidf():
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    with open('tfidf_matrix.pkl', 'rb') as f:
        matrix = pickle.load(f)

    return vectorizer, matrix


# Train a similarity-based model using the loaded TF-IDF matrix
def train_similarity_model():
    vectorizer, matrix = load_tfidf()
    cosine_sim = linear_kernel(matrix, matrix)
    return cosine_sim

# Function to get recommendations based on user input using the pre-trained model
# Function to get recommendations based on user input using the pre-trained model
def get_recommendations(user_input):
    # Load data
    df = load_data()

    # Filter dataset based on user preferences
    wine_type = user_input['wine_type']
    country = user_input['country']
    min_price, max_price = user_input['price']
    selected_occasion = user_input['occasion']  # Extract selected occasion

    # Filter recommendations based on user preferences
    filtered_recommendations = df[
        (df['price'] >= min_price) &  # Filter by minimum price
        (df['price'] <= max_price)
    ]

    # Handle 'I don't know' cases for wine type and country
    if wine_type != "I don't know":
        filtered_recommendations = filtered_recommendations[filtered_recommendations['wine_type'] == wine_type]
    if country != "I don't know":
        filtered_recommendations = filtered_recommendations[filtered_recommendations['country'] == country]

    # New: Filter recommendations based on selected occasion
    if selected_occasion == 'Anniversary' or selected_occasion == 'Birthday':
        filtered_recommendations = filtered_recommendations[filtered_recommendations['wine_type'] == 'Sparkling']
    elif selected_occasion == 'Summer Pool party':
        filtered_recommendations = filtered_recommendations[filtered_recommendations['wine_type'] == 'Rosé']
    elif selected_occasion == 'Professional diner':
        filtered_recommendations = filtered_recommendations[filtered_recommendations['wine_type'] == 'Red']
    elif selected_occasion == 'Brunch':
        filtered_recommendations = filtered_recommendations[
            (filtered_recommendations['wine_type'] == 'Rose') | (filtered_recommendations['wine_type'] == 'White')
        ]
    elif selected_occasion == 'Seafood restaurant':
        filtered_recommendations = filtered_recommendations[filtered_recommendations['wine_type'] == 'White']
    elif selected_occasion == 'Steakhouse restaurant':
        filtered_recommendations = filtered_recommendations[filtered_recommendations['wine_type'] == 'Red']
    elif selected_occasion == 'Date':
        date_wines = ['Merlot', 'Cabernet Sauvignon', 'Pinot Noir', 'Syrah']
        sparkling_wines = ['Sparkling']
        df_filtered_date = df[
            (df['wine_variety'].str.contains('|'.join(date_wines))) |
            (df['wine_type'].isin(sparkling_wines))
        ]
        filtered_recommendations = pd.concat([filtered_recommendations, df_filtered_date])
    elif selected_occasion == 'To bring to a Dinner Party':
        dinner_party_wines = ['Pinot Grigio', 'Sauvignon Blanc', 'Cabernet', 'Pinot Noir']
        df_filtered_dinner_party = df[
            (df['title'].str.contains('|'.join(dinner_party_wines)))
        ]
        filtered_recommendations = pd.concat([filtered_recommendations, df_filtered_dinner_party])

    # Remove duplicates that might occur due to concatenation
    filtered_recommendations = filtered_recommendations.drop_duplicates()

    # If no matches found after filtering, return None or an appropriate message
    if filtered_recommendations.empty:
        return None

    # Use the machine learning model to suggest wines
    vectorizer, matrix = load_tfidf()
    user_input_matrix = vectorizer.transform([user_input['preproc_description']])
    similarity_scores = linear_kernel(user_input_matrix, matrix[filtered_recommendations.index]).flatten()
    top_indices = similarity_scores.argsort()[:-15:-1]  # Retrieve top 5 indices

    recommendations = filtered_recommendations.iloc[top_indices]

    # If no matches found after filtering and similarity scoring, return None or an appropriate message
    if recommendations.empty:
        return None

    # Otherwise, return the top recommendations based on some criteria (e.g., highest ratings)
    top_recommendations = recommendations.nlargest(10, 'points')  # Retrieve top 10 recommendations

    return top_recommendations
