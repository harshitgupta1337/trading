#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source $SCRIPT_DIR/../venv/bin/activate

mkdir -p ./plots
mkdir -p ./data

BATCH_SIZE=8
tickers_file=$1
ALL_TICKERS=$(cat $tickers_file)

# Converting the NUM_TICKERS multi-line string into an array
SAVEIFS=$IFS   # Save current IFS (Internal Field Separator)
IFS=$'\n'      # Change IFS to newline char
ALL_TICKERS=($ALL_TICKERS) # split the `names` string into an array by the same name
IFS=$SAVEIFS   # Restore original IFS

NUM_TICKERS=${#ALL_TICKERS[*]}
echo $NUM_TICKERS

idx=0
while [ $idx -lt $NUM_TICKERS ]
do
    batch=""
    curr_batch_size=0
    for (( ; idx<NUM_TICKERS && curr_batch_size<BATCH_SIZE; idx++ ))
    do
        batch="$batch ${ALL_TICKERS[$idx]}"
        curr_batch_size=$((curr_batch_size+1))
    done

    # Process the batch
    pids=""
    for ticker in $batch
    do
        echo "Launching plotting for ticker $ticker"
        python3 $SCRIPT_DIR/plot_candlesticks.py -O ./plots/ -T $ticker > /dev/null &
        pids="$pids $!"
    done
    for pid in $pids
    do
        wait $pid
    done
done


