#!/bin/bash

source ./venv/bin/activate

# Get all the categories
categories=$(ls ./tickers/*)

for category in $categories; do
  ./candlesticks/plot_multi_charts.sh $category
done
