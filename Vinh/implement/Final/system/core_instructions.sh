# Define directory and files
export PCAP_DIR="./temp_storage/traffic" # Store raw PCAP files
export CSV_DIR="./temp_storage/csv" # STore CSV files
export CSV_EXTRACTED_DIR="./temp_storage/csv_extracted" # Store extracted CSV files
export CSV_PREPROCESSED_DIR="./temp_storage/csv_preprocessed" # Store preprocessed CSV files
export CSV_ATTACKER_IPS_DIR="./temp_storage/csv_attacker_ips" # Store attacker IP address CSV files

# Create directories
mkdir -p $PCAP_DIR $CSV_DIR $CSV_EXTRACTED_DIR $CSV_PREPROCESSED_DIR $CSV_ATTACKER_IPS_DIR

while FILE=$(inotifywait -e close_write --format "%w%f" "$PCAP_DIR"); do
    BASENAME=$(basename "$FILE" .pcap)

    # Convert pcap file to csv file (6 features)
    tshark -r "$FILE" \
            -T fields -e _ws.col.No. \
            -e _ws.col.Time -e ip.src \
            -e ip.dst -e _ws.col.Protocol \
            -e _ws.col.Length -e _ws.col.Info \
            -E separator=, -E occurrence=f -E quote=d \
            > "${CSV_DIR}/${BASENAME}.csv"
    export CSV_BRIDGE="${CSV_DIR}/${BASENAME}.csv"

    # Extract features from csv file (6 features) to create a new csv file (30 features)
    export CSV_EXTRACTED_BRIDGE=$(python tool.py)

    # Preprocessing the csv file(Drop unneeded column + encoding)
    export CSV_PREPROCESSED_BRIDGE=$(python preprocessing.py)

    # Predict the label of the csv file (30 features)
    python3 model_inworking.py
    if [[ $? -ne 0 ]]; then
        echo "Error: Model prediction failed for ${CSV_PREPROCESSED_BRIDGE}."
        continue
    fi

    echo "Processing for ${BASENAME} completed successfully."

done &

# For tcpdump
if [[ $# -eq 1 ]]; then 
	NETWORK_INTERFACE=$1
else
	NETWORK_INTERFACE=eth0
fi

# Capture packets from a network interface every 5s
echo "Start capturing packets from network interface $NETWORK_INTERFACE"
sudo tcpdump -i $NETWORK_INTERFACE -G 5 -w "${PCAP_DIR}/traffic-%Y-%m-%d-%H-%M-%S.pcap"
# Option:
    # -i: interface
    # -G: rotate the output file every 5s
    # -w: write the output to a file path




