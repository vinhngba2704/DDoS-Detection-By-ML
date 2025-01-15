import pandas as pd
from pathlib import Path
import os

# Path to input file
input_file = os.getenv("CSV_EXTRACTED_BRIDGE")

file_name = os.path.basename(input_file)

# # Path to output file
output_file = f"{Path(__file__).parent}/labeled_{file_name}"

df_train = pd.read_csv(input_file)
ips_to_keep = [ #Attacker
    "192.168.1.3", "192.168.1.7", "192.168.1.41", "192.168.1.23",
    # User
    "192.168.1.124", "192.168.1.147", "192.168.1.114", "192.168.1.25"]

new_df_train = df_train[df_train['Src IP'].isin(ips_to_keep)].copy()
# new_df_train = df_train.copy()

benign_ips = ["192.168.1.124", "192.168.1.147", "192.168.1.114", "192.168.1.25"]
new_df_train['label'] = 'ATTACKER'

new_df_train.loc[df_train['Src IP'].isin(benign_ips), 'label'] = 'BENIGN'
new_df_train.to_csv(output_file, index=False)
print(output_file)