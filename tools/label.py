import csv
import sys

if len(sys.argv) != 3:
    fpackets = sys.argv[1]
    fattackers = sys.argv[2]
    srccol = 1  # Assuming that the Source column is the 2nd column

    if not fpackets.endswith('.csv'):
        print("Packet file must be in CSV format")
        exit()

    # Read the existing CSV file and store its content
    with open(fpackets, 'r') as file:
        reader = csv.reader(file)
        packets = list(reader)

    # Read file of attackers' IP
    attackers = []
    print("Attackers found:")
    with open(fattackers, 'r') as file:
        for line in file:
            attackers.append(line)
            print(line)

    # Add the new column header to the first row of the data
    packets[0].append('Attacker')

    # Add values to the new column depending on whether the packet is from an attacker or not
    for i in range(1, len(packets)):
        if packets[i][srccol] in attackers:
            packets[i].append('1')
        else:
            packets[i].append('0')

    fpackets_new = fpackets.replace(".csv", "_new.csv")
    # Write the updated data back to the CSV file
    with open(fpackets_new, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(packets)
else:
    print("Usage: label.py <packet file> <attacker file>")