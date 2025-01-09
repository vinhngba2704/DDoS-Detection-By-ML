#!/bin/bash
# Load the parameters from parameter_initialization.sh
. ./parameter_initialization.sh

# The process of core_instructions.sh start from here
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

    # Clone extracted csv file for further labeling
    FILENAME=$(basename "$CSV_EXTRACTED_BRIDGE")
    cp "$CSV_EXTRACTED_BRIDGE" "$CSV_CLONE_FOR_FURTHER_LABEL_DIR/$FILENAME.temp"
    mv "$CSV_CLONE_FOR_FURTHER_LABEL_DIR/$FILENAME.temp" "$CSV_CLONE_FOR_FURTHER_LABEL_DIR/$FILENAME"

    # Preprocessing the csv file(Drop unneeded column + encoding)
    export CSV_PREPROCESSED_BRIDGE=$(python preprocessing.py)

    # Predicting the label of the csv file (30 features)
    export CSV_PREDICTED_BRIDGE=$(python model_inworking.py)
    if [[ $? -ne 0 ]]; then
        echo "Error: Model prediction failed for ${CSV_PREPROCESSED_BRIDGE}."
        continue
    fi

    # Extracting the attacker ip addresses of the predicted csv file
    python extracting_ip.py

    echo "Processing for ${BASENAME} completed successfully."

done &

# Capture packets from a network interface every 5s
echo "Start capturing packets from network interface $NETWORK_INTERFACE"
sudo tcpdump -i $NETWORK_INTERFACE -G 5 -w "${PCAP_DIR}/traffic-%Y-%m-%d-%H-%M-%S.pcap"
# Option:
    # -i: interface
    # -G: rotate the output file every 5s
    # -w: write the output to a file path




