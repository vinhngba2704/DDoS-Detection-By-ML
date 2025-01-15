import pandas as pd
from pathlib import Path
import os

# Path to input file
input_file = [
    os.getenv("INPUT_FILE_fw1", "/media/Personal/Project/DDoS_attack/Data/InternalData/fw1.csv"),
    os.getenv("INPUT_FILE_fw2", "/media/Personal/Project/DDoS_attack/Data/InternalData/fw2.csv"),
    os.getenv("INPUT_FILE_fw3", "/media/Personal/Project/DDoS_attack/Data/InternalData/fw3.csv"),
    os.getenv("INPUT_FILE_fw4", "/media/Personal/Project/DDoS_attack/Data/InternalData/fw4.csv")
]
for i in range(len(input_file)):
    file_name = input_file[i].split("/")[-1]

    # Path to output file
    output_file = f"{Path(__file__).parent}/updated_{file_name}"

    df_train = pd.read_csv(input_file[i])
    ips_to_keep = [ # fw1 and fw2
                    '192.168.1.124', '192.168.1.148', '192.168.1.216', 
                    '192.168.1.225', '192.168.1.24', '192.168.1.41', 
                    '192.168.1.45', '192.168.1.79',
                    # fw3 and fw4
                    '192.168.230.63', '192.168.230.169', '192.168.230.204', 
                    '192.168.230.153', '192.168.230.172', '192.168.230.8', 
                    '192.168.230.54', '192.168.230.216']

    new_df_train = df_train[df_train['Source'].isin(ips_to_keep)].copy()

    benign_ips = [  # fw1 and fw2
                    '192.168.1.124', '192.168.1.148', '192.168.1.79', '192.168.1.225',
                    # fw3 and fw4
                    '192.168.230.172', '192.168.230.8', '192.168.230.54', '192.168.230.216' ]
    new_df_train['label'] = 'ATTACKER'

    new_df_train.loc[df_train['Source'].isin(benign_ips), 'label'] = 'BENIGN'
    new_df_train.to_csv(output_file, index=False)
    print(f"{file_name} has been labeled and save into updated_{file_name}.csv")