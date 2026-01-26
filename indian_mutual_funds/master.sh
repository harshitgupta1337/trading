#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

cd $SCRIPT_DIR

# Step 1: Fetch scheme codes
$SCRIPT_DIR/fetch_scheme_codes.sh

for days in 180 365 730 1825; do
    # Step 2: Pull data
    python3 pull_data.py -S ./schemes.txt -N $days -D ./data/data_$days/
    # Step 3: Plot data
    python3 plot_data.py -D ./data/data_$days/ -P ./plots/days_$days/ -S ./scheme_mappings.json
    convert ./plots/days_$days/*.png ./plots/plot_days_$days.pdf
done

