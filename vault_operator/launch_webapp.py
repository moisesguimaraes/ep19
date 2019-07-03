import json
import os
import random
import subprocess

from castellan import key_manager
from castellan.common.objects.opaque_data import OpaqueData
from oslo_config import cfg

conf = cfg.ConfigOpts()
conf(["--config-file=castellan_root.conf"])

km = key_manager.API(conf)

# persist database credentials to vault and create mapping file
with open("cred.json", "r") as cred:
    credentials = json.load(cred)

    username_id = km.store("ctx", OpaqueData(
        credentials["data"]["username"].encode()
    ))

    password_id = km.store("ctx", OpaqueData(
        credentials["data"]["password"].encode()
    ))

    with open("mapping.conf", "w") as mapping_file:
        mapping_file.write("\n".join([
            "[db]",
            f"username={username_id}",
            f"password={password_id}"
        ]))

# inject vault token via env config OS_{group}__{name}
with open("token.json", "r") as token_json:
    token = json.load(token_json)

    os.environ["OS_VAULT__ROOT_TOKEN_ID"] = token["auth"]["client_token"]

# run webapp
subprocess.run([
    "python", "../app/app.py",
    f"--app-port={random.randint(5050, 5099)}",
    "--config-file=webapp.conf"
])
