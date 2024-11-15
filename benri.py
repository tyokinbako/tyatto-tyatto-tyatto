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
    memo_tati =Memo.select()
    return render_template("memonope-zi.html",memo_tati = memo_tati)

@haru.route("/memo1", methods=["POST"])
def memo1():
    memo=request.form.get("memo")
    Memo.create(memo=memo)
    return redirect("/memo")

@haru.route("/memo_keshi/<id>", methods=["POST"])
def memo_keshi(id):
    memo = Memo.get(id=id)
    memo.delete_instance()
    return redirect("/memo")
    
haru.run(debug=True, host="0.0.0.0")

