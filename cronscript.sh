#!/bin/bash

# Setup the cron job using following config in crontab -e
# 0 14 * * * /home/ubuntu/git/trading/cronscript.sh

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

./plot-categories.sh && ./merge-categories.sh
