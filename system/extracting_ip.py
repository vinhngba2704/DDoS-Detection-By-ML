import pandas as pd
import os

input_file = os.getenv("CSV_PREDICTED_BRIDGE")
basename = os.path.basename(input_file)
base_dir = os.getenv("CSV_ATTACKER_IPS_DIR")
output_file = os.path.join(base_dir, f"attacker_ips_{basename}")

data = pd.read_csv(input_file)
attacker_ips = data[data["label"] == 1]['Src IP']

with open(output_file, "w") as file:
    for ip in attacker_ips:
        file.write(f"{ip}\n")