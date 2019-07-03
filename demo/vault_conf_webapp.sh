#!/bin/bash

echo -e "\nRunning webapp with conf:\n"

cat web_vault.conf

echo -e "\n"

OS_VAULT__ROOT_TOKEN_ID=s.FSUHTpovzLBhu4ENA5evXWdC \
python ../app/app.py --config-file=web_vault.conf