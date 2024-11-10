from flask import Flask
from flask import render_template

from flask import redirect
from flask import request
from hanage import Memo

haru = Flask(__name__)

@haru.route("/kobiru")
def okane():
    return render_template("kobirunope-zi.html")

@haru.route("/tyato")
def unti():
    return render_template("tyatonope-zi.html")

@haru.route("/memo", methods=["GET", "POST"])
def WC():
    text=""
    if request.method == "POST" :
        text = request.form["input_text"]


    return render_template("memonope-zi.html",text = text)

@haru.route("/memo1", methods=["POST"])
def memo1():
    memo=request.form.get("memo")
    Memo.create(memo=memo)
    return redirect("/memo")
                    
haru.run(debug=True, host="0.0.0.0")

@haru.route("/memo2", methods=["GET","POST"])

def WC():
    return render_template("memonope-zi.html")

