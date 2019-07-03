#!/bin/bash

echo -e "\nRunning webapp with conf:\n"

cat web_plaintext.conf

echo -e ""

python ../app/app.py --config-file=web_plaintext.conf