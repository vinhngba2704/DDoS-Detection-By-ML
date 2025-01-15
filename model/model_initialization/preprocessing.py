import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from CustomEncoderLabel import encode_label, decode_label
from CustomEncoder import CustomLabelEncoder
import os
from pathlib import Path

input_file = os.getenv("CSV_LABELED_BRIDGE")
basename = os.path.basename(input_file)
output_file = f"{Path(__file__).parent}/preprocessed_{basename}"

data = pd.read_csv(input_file)

# Drop unneeded columns
# + "Flow ID"
# + "Src IP"
# + "Src Port"
# + "Dst IP"
# + "Dst Port"
data = data.drop(columns= ['Flow ID', 'Src IP', 'Src Port', 'Dst IP', 'Dst Port'])

# Define encoder for feature columns
encoder = CustomLabelEncoder()
data['Protocol'] = encoder.fit_transform(data['Protocol'])

# Encode the label column
data = encode_label(data)

# Output to preprocessed file
data.to_csv(output_file, index=False)
print(output_file)


