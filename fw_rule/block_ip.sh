#!/bin/bash

ipset_name="blacklist"

#Create set with applying timeout to block IP in a particular period
#/dev/null - redirect all stdout and stderr
if ! sudo ipset list $ipset_name &>/dev/null;then
    sudo ipset create blacklist hash:ip timeout 120
else 
    echo "Set $ipset_name has already exist"
fi

#Directory storing the attacker ips file
watch_dir="../Vinh/implement/Final/system/temp_storage/csv_attacker_ips"

read_and_add_ips(){
    local file="$1"

    #Check whether file is empty or not
    if [[ ! -s "$file" ]]; then 
        echo "File $file empty."
        return
    fi

    #Reading each line in file
    echo "-------------------------------------------------------------------"
    echo "Reading file $file"
    while read -r ip; do 
        #Pass if line is empty or is "nan"
        if [[ -z "$ip" || "$ip" == "nan" ]]; then
            continue
        fi
        #exist -> return 0, non-exist -> other 
        if ! sudo ipset test $ipset_name $ip &>/dev/null; then
            sudo ipset add $ipset_name $ip
            echo "Added $ip to the blacklist"
        else
            echo "IP $ip already exists, skipping."
        fi
    done < "$file"
}

#When new file added into folder read_and_add_ips function will be called
#timeout 120 - script will stop if it does not have change in 120s
inotifywait -m -e create --timeout 120 --format "%w%f" "$watch_dir" | while read -r new_file; do
    read_and_add_ips "$new_file"

done


