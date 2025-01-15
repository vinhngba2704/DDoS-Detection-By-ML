#!/bin/bash
# Define directory and files
export PCAP_DIR="./temp_storage/traffic"
export CSV_DIR="./temp_storage/csv"
export CSV_EXTRACTED_DIR="./temp_storage/csv_extracted"
export CSV_PREPROCESSED_DIR="./temp_storage/csv_preprocessed"
export CSV_PREDICTED_DIR="./temp_storage/csv_predicted"
export CSV_ATTACKER_IPS_DIR="./temp_storage/csv_attacker_ips"
export CSV_CLONE_FOR_FURTHER_LABEL_DIR="./temp_storage/csv_clone"

# For tcpdump
NETWORK_INTERFACE=wlp0s20f3

# Create directory to store raw pcap files
mkdir -p $PCAP_DIR
# Create directory to store csv files
mkdir -p $CSV_DIR
# Create directory to store extracted csv files
mkdir -p $CSV_EXTRACTED_DIR
# Create directory to store preprocessed csv files
mkdir -p $CSV_PREPROCESSED_DIR
# Create directory to store predicted csv files
mkdir -p $CSV_PREDICTED_DIR
# Create directory to store attacker ip address csv files
mkdir -p $CSV_ATTACKER_IPS_DIR
# Create directory to store copy version of extracted csv files for further labeling
mkdir -p $CSV_CLONE_FOR_FURTHER_LABEL_DIR

echo "Successfully initialize needed parameters"