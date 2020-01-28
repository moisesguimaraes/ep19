import os

from flask import Flask, render_template
from oslo_config import cfg
import psycopg2

app_dir = os.path.dirname(os.path.realpath(__file__))

conf = cfg.ConfigOpts()

_app_opts = [
    cfg.StrOpt("host", default="0.0.0.0"),
    cfg.IntOpt("port", default=5000),
]

_db_opts = [
    cfg.StrOpt("hostname", default="localhost"),
    cfg.StrOpt("username", required=True),
    cfg.StrOpt("password", required=True),
]

conf.register_cli_opts(_app_opts, "app")
conf.register_opts(_db_opts, "db")

conf()

app = Flask(__name__, template_folder="./templates")


@app.route("/")
def connect():
    try:
        with psycopg2.connect(
            f"dbname=postgres host={conf.db.hostname} "
            f"user={conf.db.username} password={conf.db.password}"
        ) as _:
            template = "200.html"
    except psycopg2.OperationalError:
        template = "403.html"

    return render_template(template, conf=conf)


if __name__ == "__main__":
    print(
        "### oslo.config vault env token:",
        os.environ.get("OS_VAULT__ROOT_TOKEN_ID", ""),
    )

    app.run(host=conf.app.host, port=conf.app.port)
