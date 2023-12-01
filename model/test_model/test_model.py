import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Assuming you have a DataFrame named 'data' with columns: price_range, country, aroma_notes, dryness, and target (the wine suggestion)
dataset_path = '~/code/sabrinaauger/wino/interface/wine_reviews.csv'
data = pd.read_csv(dataset_path)
# Encode categorical variables
label_encoder = LabelEncoder()
data['country'] = label_encoder.fit_transform(data['country'])
data['aroma_notes'] = label_encoder.fit_transform(data['aroma_notes'])

# Split the data into features (X) and target variable (y)
X = data[['price_range', 'country', 'aroma_notes', 'dryness']]
y = data['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Now, you can use this trained model for making wine suggestions based on user input.
