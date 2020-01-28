#!/bin/bash

echo -e "\nRunning webapp with conf:\n"

tail -n +1 app.conf castellan.conf

echo -e ""

source ../../vaultrc

set -eux

vault read -format=json database/creds/webapp-minute > cred.json

vault token create -format=json -policy=webapp -period=1m > token.json

python launch_webapp.py