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
model = joblib.load('random_forest_model.joblib')

label_pred = model.predict(data.drop(columns=["Src IP"]))
data["label"] = label_pred

# Save the predicted data to the output file
data.to_csv(output_file, index=False)

# Print the output filename
print(output_file)