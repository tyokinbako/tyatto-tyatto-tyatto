from flask import Flask
from flask import render_template
haru = Flask(__name__)
@haru.route("/tyatto")
def tatemono():
    return render_template("tyattonope-zi.html")
haru.run(debug=True)