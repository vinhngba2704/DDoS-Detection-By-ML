# Data Source: Internal System

# Initialize input paths

# fw1
export INPUT_FILE_fw1="/media/Personal/Project/DDoS_attack/Data/InternalData/fw1.csv"

# fw2
export INPUT_FILE_fw2="/media/Personal/Project/DDoS_attack/Data/InternalData/fw2.csv"

# fw3
export INPUT_FILE_fw3="/media/Personal/Project/DDoS_attack/Data/InternalData/fw3.csv"

# fw4
export INPUT_FILE_fw4="/media/Personal/Project/DDoS_attack/Data/InternalData/fw4.csv"

# Labling
python labeling.py

# Transform from 7 basic features to 31 features
python 7basic_to_31-FlowAssemble_convert.py


