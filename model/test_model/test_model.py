# Example preprocessing using pandas
import os
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
df = pd.read_csv("~/code/sabrinaauger/wino/raw_data/winemag-data_first150k.csv")

# Keep only the relevant columns
selected_columns = ['country', 'price', 'variety']
df = df[selected_columns]

# Drop rows with missing values
df = df.dropna()

# Encode categorical variables
le = LabelEncoder()
df['country'] = le.fit_transform(df['country'])
df['variety'] = le.fit_transform(df['variety'])

# Normalize numerical features
scaler = StandardScaler()
df[['price']] = scaler.fit_transform(df[['price']])

# Extract features
X = df[['country', 'price', 'variety']]

# Create and navigate to the model directory
model_folder = os.path.join(os.getcwd(), "wine_recommendation_model")
os.makedirs(model_folder, exist_ok=True)
os.chdir(model_folder)

# Initialize and train the model
model = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
model.fit(X)

# Now, when a user provides their preferences, you can find the nearest wines in the dataset
user_preferences = pd.DataFrame({'country': ['France'], 'price': [25], 'variety': ['Merlot']})
user_preferences['country'] = le.transform(user_preferences['country'])
user_preferences['variety'] = le.transform(user_preferences['variety'])
user_preferences[['price']] = scaler.transform(user_preferences[['price']])

# Find the nearest wines
_, indices = model.kneighbors(user_preferences)

# Display recommended wines
recommendations = df.iloc[indices[0]]
print("Recommended Wines:")
print(recommendations)
