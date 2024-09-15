from flask import Flask
from flask import render_template

haru = Flask(__name__)

@haru.route("/kobiru")
def okane():
    return render_template("kobirunope-zi.html")

@haru.route("/tyato")
def unti():
    return render_template("tyatonope-zi.html")

haru.run(debug=True, host="0.0.0.0")