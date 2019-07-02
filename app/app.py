import os

from flask import Flask
from oslo_config import cfg
import psycopg2

app_dir = os.path.dirname(os.path.realpath(__file__))

conf = cfg.ConfigOpts()

_app_opts = [
    cfg.StrOpt('host', default="0.0.0.0"),
    cfg.IntOpt('port', default=5000),
]

_db_opts = [
    cfg.StrOpt('hostname', default="db"),
    cfg.StrOpt('username', default="postgres"),
    cfg.StrOpt('password', default="changeme")
]

conf.register_cli_opts(_app_opts, "app")
conf.register_opts(_db_opts, "db")

conf()

app = Flask(__name__)


@app.route('/')
def connect():
    try:
        conn = psycopg2.connect(
            f"dbname=postgres host={conf.db.hostname} "
            f"user={conf.db.username} password={conf.db.password}"
        )

        status = "✅ Successfully connected"
        conn.close()
    except psycopg2.OperationalError:
        with open(os.path.join(app_dir, "403.html")) as response:
            return response.read()

    return (
        f"{status} to DB at <em>{conf.db.hostname}</em> with:<br/><br/>"
        f"&nbsp;&nbsp;&nbsp; username: <em>{conf.db.username}</em><br/>"
        f"&nbsp;&nbsp;&nbsp; password: <em>{conf.db.password}</em><br/>"
    )


if __name__ == "__main__":
    app.run(host=conf.app.host, port=conf.app.port)
