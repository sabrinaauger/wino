import gensim
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import nltk

# Load the dataset
dataset_path = '~/code/sabrinaauger/wino/interface/wine_reviews.csv'
wine_df = pd.read_csv(dataset_path)

# Load stop words
stop_words = set(stopwords.words('english'))

# Tokenize the description column of current DF and create new ones
wine_df['description_tokenized'] =wine_df['description'].apply(word_tokenize)

wine_df['description_filtered'] = wine_df['description_tokenized'].apply(lambda x: [word for word in x if word.lower() not in stop_words])

# Sorting which feature is what
y = ['designation']
categorical_features_list = ['country', 'province', 'region_1', 'region_2', 'variety', 'winery']
text_features_list = ['taster_name', 'taster_twitter_handle', 'title']
numerical_features_list = ['points', 'price']
# country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery

# Vectorizing numeric features
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numeric_scaled = scaler.fit_transform(wine_df[numerical_features_list])
wine_df_scaled = pd.concat([wine_df, pd.DataFrame(numeric_scaled, columns=['points_scaled', 'price_scaled'])], axis=1)

# Vectorizing categorical features
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()

category_encoded = encoder.fit_transform(wine_df[categorical_features_list]).toarray()
wine_df_scaled = pd.concat([wine_df, pd.DataFrame(category_encoded, columns=encoder.get_feature_names_out(categorical_features_list))], axis=1)

# # Extract the 'description' column
# descriptions = wine_df['description'].dropna().tolist()

# # Tokenize the descriptions
# tokenized_descriptions = [simple_preprocess(desc) for desc in descriptions]

# # Train a Word2Vec model
# model = Word2Vec(sentences=tokenized_descriptions, vector_size=100, window=5, min_count=1, workers=4)

# # Save the model to a file
# model.save('word2vec_model.bin')
