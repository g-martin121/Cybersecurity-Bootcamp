#!/bin/bash
# Guided Lab: Loop through log files
for file in *.log; do
    if [ -f "$file" ]; then
        echo "Processing $file"
        grep "error" "$file" | head -n 2
    fi
done
