#!/bin/bash

# Check if NAVAll.TXT already exists, if not then download it
if [ ! -f NAVAll.TXT ]; then
    wget -O NAVAll.TXT -c https://portal.amfiindia.com/spages/NAVAll.TXT
    if [ $? -ne 0 ]; then
        echo "Failed to download NAVAll.TXT"
        exit 1
    fi
fi

# Filter only those lines that contain scheme codes (assuming scheme codes are numeric and 6 digits long)

# regular expression for integers separated by semicolon
regexp='^[0-9]*;'
cat NAVAll.TXT | grep -E $regexp
