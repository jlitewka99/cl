#!/bin/bash

mkdir singlepages


find out -type f -iname \*.png -delete

find singlepages -type f -iname \*.png -delete

rm out.png 

python3 b.py