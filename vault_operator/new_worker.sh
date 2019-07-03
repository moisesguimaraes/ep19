#!/bin/bash

source vaultrc

set -eux

vault read -format=json database/creds/webapp-minute > cred.json

vault token create -format=json -policy=webapp -period=1m > token.json

python launch_webapp.py