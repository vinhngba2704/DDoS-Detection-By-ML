source core_instruction.sh

# Exporting the watching directory for inotify
export WATCHING_DIR="/temp_storage/csv_clone"
# Exporting the pre-defined threshold
export THRESHOLD=0.5
# Exporting a variable for counting the file that have accuracy lower than threshold
export COUNT=0


while export FILE=$(inotifywait -e close_write --format "%w%f" "$WATCHING_DIR"); do
    # Ignore the tempory file of copy process, only file of mv process pass
    if [["$FILE" == *.temp]]; then
        continue
    fi

    # Notice that the file has been labeled
    FILENAME=$(basename "$FILE")
    echo "File $FILENAME has been labeled".

    export accuracy_score=$(python accuracy_calculating.py)
    # Handling if accuracy_score is greater than threshold
    if (( $(echo "$accuracy_score >= $THRESHOLD" | bc -l) )); then
        continue
    
    # Handling if accuracy_score is lower than threshold
    else
        # Adding action here
        # 1. Stop the process of core_instructions.sh
        # 2. Triggering the alternative rule_temporary.sh
        # 3. Triggering the model_reinitialization.sh
        # 4. Stop the process of alternative rule_temporary.sh
        # 5. Triggering the core_instruction.sh again

    fi

done