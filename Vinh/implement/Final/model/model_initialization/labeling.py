import pandas as pd
from pathlib import Path
import os

# Path to input file
input_file = os.getenv("CSV_EXTRACTED_BRIDGE")

file_name = os.path.basename(input_file)

# # Path to output file
output_file = f"{Path(__file__).parent}/labeled_{file_name}"

df_train = pd.read_csv(input_file)
ips_to_keep = [ # fw1 and fw2
                '192.168.1.124', '192.168.1.148', '192.168.1.216', 
                '192.168.1.225', '192.168.1.24', '192.168.1.41', 
                '192.168.1.45', '192.168.1.79',
                # fw3 and fw4
                '192.168.230.63', '192.168.230.169', '192.168.230.204', 
                '192.168.230.153', '192.168.230.172', '192.168.230.8', 
                '192.168.230.54', '192.168.230.216']

new_df_train = df_train[df_train['Src IP'].isin(ips_to_keep)].copy()

benign_ips = [  # fw1 and fw2
                '192.168.1.124', '192.168.1.148', '192.168.1.79', '192.168.1.225',
                # fw3 and fw4
                '192.168.230.172', '192.168.230.8', '192.168.230.54', '192.168.230.216' ]
new_df_train['label'] = 'ATTACKER'

new_df_train.loc[df_train['Src IP'].isin(benign_ips), 'label'] = 'BENIGN'
new_df_train.to_csv(output_file, index=False)
print(output_file)