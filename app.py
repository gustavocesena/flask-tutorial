from flask import Flask

app = Flask(__name__)


@app.route("/cari")
def hello_world():
    return 5/0

