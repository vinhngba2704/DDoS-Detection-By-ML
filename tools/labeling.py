import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_train = pd.read_csv("/home/ubuntu/DDoS-Detection-By-ML/pcap_file/firewall/fw2.csv")
ips_to_keep = ['192.168.1.124', '192.168.1.148', '192.168.1.216', 
               '192.168.1.225', '192.168.1.24', '192.168.1.41', 
               '192.168.1.45', '192.168.1.79']

new_df_train = df_train[df_train['Source'].isin(ips_to_keep)]

benign_ips = ['192.168.1.124', '192.168.1.148', '192.168.1.79', '192.168.1.225']

new_df_train['label'] = 'ATTACKER'

new_df_train.loc[df_train['Source'].isin(benign_ips), 'label'] = 'BENIGN'
new_df_train.to_csv('/home/ubuntu/DDoS-Detection-By-ML/pcap_file/firewall/updated_fw2.csv', index=False)
