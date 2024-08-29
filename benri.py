from flask import Flask
from flask import render_template
haru = Flask(__name__)

@haru.route("/kobiru")
def okane():
    return render_template("kobirunope-zi.html")

@haru.route("/tyatto")
def tyatto():
    return render_template("tyattonope-zi.html")
haru.run(host="0.0.0.0")