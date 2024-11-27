import random
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import mutual_info_classif

# Load dataset
data = pd.read_csv('/home/ubuntu/year3/group_project/extracted_flow_features.csv')

# Drop flag columns 
flag_columns = [
    'FIN Flag Count', 'SYN Flag Count', 'RST Flag Count', 'PSH Flag Count',
    'ACK Flag Count', 'URG Flag Count', 'CWR Flag Count', 'ECE Flag Count'
]
data = data.drop(columns=flag_columns)

# Encoding categorical columns
label_encoder = LabelEncoder()
for col in ['Flow ID', 'Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Protocol']:
    data[col] = label_encoder.fit_transform(data[col])

# Convert ports if necessary
data['Src Port'] = pd.to_numeric(data['Src Port'], errors='coerce').fillna(0).astype(int)
data['Dst Port'] = pd.to_numeric(data['Dst Port'], errors='coerce').fillna(0).astype(int)

# Randomly assign 'Label' column for demonstration (replace with real labels if available)
data['Label'] = [random.choice([0, 1]) for _ in range(len(data))]

# Separate features and target
X = data.drop('Label', axis=1)
y = data['Label']

# Calculate information gain
info_gain = mutual_info_classif(X, y, random_state=42)
feature_info = pd.DataFrame({'Feature': X.columns, 'Information Gain': info_gain})

# Sort features by descending information gain
sorted_features = feature_info.sort_values(by='Information Gain', ascending=False)
print(sorted_features)
