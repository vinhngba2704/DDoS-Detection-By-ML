PCAP_FILE="/media/Personal/Project/DDoS_attack/Data/InternalData/20241227-20250108T155938Z-001/20241227/fw1.pcap"
BASENAME=$(basename "$PCAP_FILE" .pcap)
tshark -r $PCAP_FILE \
        -T fields -e _ws.col.No. \
        -e _ws.col.Time -e ip.src \
        -e ip.dst -e _ws.col.Protocol \
        -e _ws.col.Length -e _ws.col.Info \
        -E separator=, -E occurrence=f -E quote=d \
        > "${BASENAME}.csv"
echo "PCAP to CSV completed."
export CSV_BRIDGE="${BASENAME}.csv"

# Feature extraction
export CSV_EXTRACTED_BRIDGE=$(python tool.py)
echo "Feature extraction completed."

# Labeling the csv file (+ 1 feature: Label)
export CSV_LABELED_BRIDGE=$(python labeling.py)
echo "Labeling completed."

# Preprocessing the csv file(Drop unneeded column + encoding)
export CSV_PREPROCESSED_BRIDGE=$(python preprocessing.py)
echo "Preprocessing completed."

# Model initialization
python model_initialization.py
echo "Model initialization completed."

# Copy model to system
cp random_forest_model.joblib ../../system/
echo "Copied model to system"
