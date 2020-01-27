#!/bin/bash

echo -e "\nRunning webapp with conf:\n"

tail -n +1 app.conf castellan.conf mapping.conf

echo -e ""

OS_VAULT__ROOT_TOKEN_ID=s.FSUHTpovzLBhu4ENA5evXWdC \
python ../../app/app.py --config-file=app.conf
