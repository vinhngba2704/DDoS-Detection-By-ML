# Data Source: Kaggle

# Initialize input paths

# # LDAP
# export TRAINING_INPUT_FILE="/media/Personal/Project/DDoS_attack/Data/ExternalData/csv/Kaggle/train/LDAP-training.csv"
# export TESTING_INPUT_FILE="/media/Personal/Project/DDoS_attack/Data/ExternalData/csv/Kaggle/test/LDAP-testing.csv"

# UDP
export TRAINING_INPUT_FILE="/media/Personal/Project/DDoS_attack/Data/ExternalData/csv/Kaggle/train/UDP-training.csv"
export TESTING_INPUT_FILE="/media/Personal/Project/DDoS_attack/Data/ExternalData/csv/Kaggle/test/UDP-testing.csv"

# # UDPLag
# export TRAINING_INPUT_FILE="/media/Personal/Project/DDoS_attack/Data/ExternalData/csv/Kaggle/train/UDPLag-training.csv"
# export TESTING_INPUT_FILE="/media/Personal/Project/DDoS_attack/Data/ExternalData/csv/Kaggle/test/UDPLag-testing.csv"

# Convert from >80 features to 7 basic features
python convert_tool.py 

# Convert from 7 basic features to 31 features
python tool_label.py

