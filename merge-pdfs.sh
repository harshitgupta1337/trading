#!/bin/bash

category=$1

convert ./plots/tickers/$category/*.png ./plots/categories/$category.pdf
