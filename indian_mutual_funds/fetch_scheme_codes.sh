#!/bin/bash

# Check if NAVAll.TXT already exists, if not then download it
if [ ! -f NAVAll.TXT ]; then
    wget -O NAVAll.TXT -c https://portal.amfiindia.com/spages/NAVAll.TXT
    if [ $? -ne 0 ]; then
        echo "Failed to download NAVAll.TXT"
        exit 1
    fi
fi
