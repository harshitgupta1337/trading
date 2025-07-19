#!/bin/bash

source ./venv/bin/activate

# Get all the categories
categories=$(ls ./tickers/*)

mkdir -p ./plots/categories

for category in $categories; do
  ./merge-pdfs.sh $(basename $category)
done
