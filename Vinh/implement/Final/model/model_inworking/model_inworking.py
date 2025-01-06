import joblib
import pandas as pd
import os

# Upload the original ip column
ip_input_file = os.getenv("CSV_EXTRACTED_BRIDGE")
ip_data = pd.read_csv(ip_input_file)
ip_column = ip_data["Src IP"]

input_file = os.getenv("CSV_PREPROCESSED_BRIDGE")
basename = os.path.basename(input_file)
base_dir = os.getenv("CSV_ATTACKER_IPS_DIR")
output_file = os.path.join(base_dir, f"attacker_ips_{basename}")

data = pd.read_csv(input_file)
# Load the model from the file
model = joblib.load('model.joblib')

# Predict the label for the flows
data['label'] = model.predict(data)
data['Src IP'] = ip_column

# Extract the ATTACKER ip address
attacker_ip = data[data['label'] == 1]['Src IP']

with open("attacker_ips", "w") as file:
    for ip in attacker_ip:
        file.write(f"{ip}\n")


