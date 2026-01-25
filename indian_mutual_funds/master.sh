#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

cd $SCRIPT_DIR

# Step 1: Fetch scheme codes
$SCRIPT_DIR/fetch_scheme_codes.sh

for days in 180 365 730; do
    python3 pull_data.py -S ./schemes.txt -N $days -D ./data_$days/
    python3 plot_data.py -D ./data_$days/ -P ./plots_$days/ -S ./scheme_mappings.json
    convert ./plots_$days/*.png ./plots_$days.pdf
done

