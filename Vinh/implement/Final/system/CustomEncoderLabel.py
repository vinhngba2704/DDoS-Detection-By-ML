# Define encoding list
encoding_list = {
    "ATTACKER": 1,
    "BENIGN": 0
}

def encode_label(data):
    data['label'] = data['label'].map(encoding_list)
    return data

def decode_label(data):
    encoding_list_reverse = {v: k for k, v in encoding_list.items()}
    data['label'] = data['label'].map(encoding_list_reverse)
    return data

