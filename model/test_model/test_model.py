# Example preprocessing using pandas
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
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

# Extract features and target variable
X = df[['country', 'price', 'variety']]
y = df['suggested_wine']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and navigate to the model directory
model_folder = os.path.join(dataset_folder, "test_model")
os.makedirs(model_folder, exist_ok=True)
os.chdir(model_folder)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:\n", report)
