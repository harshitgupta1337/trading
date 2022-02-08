#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source $SCRIPT_DIR/../venv/bin/activate

tickers_file=$1

pids=""
for ticker in $(cat $tickers_file)
do
    echo "Launching plotting for ticker $ticker"
    python3 plot_candlesticks.py -O ./plots/ -T $ticker > /dev/null #&
    #pids="$pids $!"
done
for pid in $pids
do
    wait $pid
done