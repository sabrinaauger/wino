import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load the dataset
data_path = '~/code/sabrinaauger/wino/raw_data/winemag-data_first150k.csv'
df = pd.read_csv(data_path)

# Select the 'description' column
descriptions = df['description']

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=100)  # Set max_features to the desired number

# Fit and transform the 'description' column
tfidf_matrix = vectorizer.fit_transform(descriptions)

# Get feature names (words) from the vectorizer
feature_names = vectorizer.get_feature_names_out()

# Create a DataFrame with the TF-IDF values for each word in each description
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# Calculate the total TF-IDF values for each word across all descriptions
total_tfidf = tfidf_df.sum()

# Sort words based on total TF-IDF values in descending order
sorted_words = total_tfidf.sort_values(ascending=False)

# Function to categorize words using spaCy
def categorize_word(word):
    token = nlp(word.lower())

    # Define categories and corresponding keywords with similarity thresholds
    categories = {
        'fruity': ['fruity', 'berry', 'ripe', 'tropical', 'citrus', 'fruit'],
        'floral': ['floral', 'perfumed', 'blossom', 'flower', 'bloom'],
        'woody': ['woody', 'oak', 'cedar', 'vanilla', 'spice', 'burned', 'burnt', 'smoky', 'wood', 'tree'],
        'herbal': ['herbal', 'tea', 'hay', 'green', 'mint', 'grass', 'leaves', 'herb']
    }

    # Calculate similarity for each category and find the one with the highest similarity
    max_similarity = 0
    selected_category = 'other'

    for category, keywords in categories.items():
        similarity = max(token.similarity(nlp(w)) for w in keywords)
        if similarity > max_similarity:
            max_similarity = similarity
            selected_category = category

    return selected_category

# Example usage
word = 'fruity'
category = categorize_word(word)
print(f'The word "{word}" belongs to the category: {category}')


# Categorize words into aromas
categorized_aromas = {
    'fruity': [],
    'floral': [],
    'woody': [],
    'herbal': []
    }

for word in sorted_words.index:
    category = categorize_word(word)
    categorized_aromas[category].append(word)

# Display categorized words
for aroma, words in categorized_aromas.items():
    print(f'{aroma.capitalize()} words: {words}')

with open('global_aromas.pkl', 'wb') as file:
    pickle.dump(categorized_aromas, file)
