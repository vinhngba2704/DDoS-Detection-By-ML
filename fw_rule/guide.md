# Installing
1. Install **ipset**:
```
sudo apt update
sudo apt install ipset -y
```
2. Install **inotifywait**
```
sudo apt update
sudo apt install inotify-tools
```

# Step to Setup
1. Create rule in iptables - block IPs in ipset set
```
sudo iptables -A FORWARD -m set --match-set blacklist src -j DROP
```
2. Run bash script before run Model bash script (when folder ./temp_storage/csv_attacker_ips is empty)
```
chmod +x block_ip.sh
./block_ip
```

# Commands
1. Check the ipset list:
```
#list all sets
sudo ipset list

#list specific set 
sudo ipset <set_name>
```

2. Delete the set
```
sudo ipset destroy <set_name>
```

3. Check rule in iptable
```
sudo iptables -L --line-numbers
```