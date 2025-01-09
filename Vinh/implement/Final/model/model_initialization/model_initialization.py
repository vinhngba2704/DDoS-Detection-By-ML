import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from sklearn.preprocessing import LabelEncoder

data_path = os.getenv("CSV_PREPROCESSED_BRIDGE")

# Load your dataset
data = pd.read_csv(data_path)

# Preprocess your data
X = data.drop(columns=['label'])
y = data['label']

# Initialize the Random Forest random_forest_model
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the random_forest_model on the entire dataset
random_forest_model.fit(X, y)

# Save the model to a file
model_filename = 'random_forest_model.joblib'
joblib.dump(random_forest_model, model_filename)
print(f'Model saved to {model_filename}')