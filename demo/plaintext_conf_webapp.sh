#!/bin/bash

echo -e "\nRunning webapp with conf:\n"

cat web_plaintext.conf

echo -e "\n"


python ../app/app.py --config-file=web_plaintext.conf