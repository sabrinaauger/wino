import json
import os
import pandas as pd
from gensim.models import Word2Vec

# Load your dataset
wine_reviews_df = pd.read_csv('~/code/sabrinaauger/wino/data/clean_data/test_wine_reviews_df.csv')

# Specify the directory containing your JSON files
aromas_directory = os.path.expanduser('~/code/sabrinaauger/wino/interface/aromas')

# Get a list of all JSON files in the directory
json_files = [file for file in os.listdir(aromas_directory) if file.endswith('.json')]

# Read and store content of each file
file_contents = {}
for file_name in json_files:
    # Create the full file path by joining the directory and file name
    file_path = os.path.join(aromas_directory, file_name)

    with open(file_path, 'r') as file:
        # Load JSON content
        content = json.load(file)

        # Create variable name based on file name
        variable_name = file_name.split('.')[0] + '_word'

        # Store content in the dictionary with variable name as the key
        file_contents[variable_name] = content

# Extract aroma lists
fruity = file_contents.get('fruity_word')
floral = file_contents.get('floral_word')
earthy = file_contents.get('earthy_word')
herbal = file_contents.get('herbal_word')

# Training data
training_data = [description.split() for description in wine_reviews_df['description']]

# Train the Word2Vec model
model = Word2Vec(sentences=training_data, vector_size=100, window=5, min_count=1, workers=4)

# Create a dictionary to store similar words for each aroma
similar_aromas = {
    'fruity': [w for word in fruity if word in model.wv.key_to_index for w, _ in model.wv.most_similar(word)],
    'floral': [w for word in floral if word in model.wv.key_to_index for w, _ in model.wv.most_similar(word)],
    'earthy': [w for word in earthy if word in model.wv.key_to_index for w, _ in model.wv.most_similar(word)],
    'herbal': [w for word in herbal if word in model.wv.key_to_index for w, _ in model.wv.most_similar(word)],
}

fruity_words = similar_aromas['fruity']
floral_words = similar_aromas['floral']
herbal_words = similar_aromas['herbal']
earthy_words = similar_aromas['earthy']


def check_aromas(description):
    description_lower = description.lower()
    for word in fruity_words:
        if word in description_lower:
            return 'Fruity'
            break
    for word in floral_words:
            return 'Floral'
            break
    for word in herbal_words:
            return 'Herbal'
            break
    for word in earthy_words:
            return 'Earthy'
            break
    return None

wine_reviews_df['aroma'] = wine_reviews_df['description'].apply(check_aromas)

wine_reviews_df.to_csv('~/code/sabrinaauger/wino/data/clean_data/test_wine_reviews_df.csv', index=False)
