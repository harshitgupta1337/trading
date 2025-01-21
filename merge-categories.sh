#!/bin/bash

source ./venv/bin/activate

# Get all the categories
categories=$(ls ./tickers/*)

for category in $categories; do
  ./merge-pdfs.sh $(basename $category)
done
