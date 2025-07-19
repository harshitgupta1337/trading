#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

./plot-categories.sh && ./merge-categories.sh

mkdir -p /plots/
rm -rf /plots/*
mv ./plots/categories/* /plots/
