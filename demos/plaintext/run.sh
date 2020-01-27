#!/bin/bash

echo -e "\nRunning webapp with conf:\n"

cat app.conf

echo -e ""

python ../../app/app.py --config-file=app.conf
