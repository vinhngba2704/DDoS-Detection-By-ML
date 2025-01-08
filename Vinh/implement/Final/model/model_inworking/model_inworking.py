import joblib
import pandas as pd
import os

# Upload the original ip column
ip_input_file = os.getenv("CSV_EXTRACTED_BRIDGE")
ip_data = pd.read_csv(ip_input_file)
ip_column = ip_data["Src IP"]

input_file = os.getenv("CSV_PREPROCESSED_BRIDGE")
basename = os.path.basename(input_file)
base_dir = os.getenv("CSV_PREDICTED_DIR")
output_file = os.path.join(base_dir, f"predicted_{basename}")

# Read the data and add the 'Src IP' column
data = pd.read_csv(input_file)
data['Src IP'] = ip_column

# Load the model from the file
model = joblib.load('model.joblib')

# Create an empty list to store the predicted rows
predicted_rows = []

# Iterate through the DataFrame rows and predict the label for each row
for _, row in data.iterrows():
    # Prepare the features (X), excluding 'label' and 'Src IP'
    X = {col: row[col] for col in data.columns if col not in ["label", "Src IP"]}
    
    # Predict the label for the current row
    y_pred = model.predict_one(X)

    # Assign the predicted label to the row
    row["label"] = y_pred
    
    # Add the row to the list of predicted rows
    predicted_rows.append(row)

# Convert the list of predicted rows back to a DataFrame
predicted_data = pd.DataFrame(predicted_rows)

# Save the predicted data to the output file
predicted_data.to_csv(output_file, index=False)

# Print the output filename
print(output_file)