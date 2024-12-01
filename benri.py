from flask import Flask
from flask import render_template

from flask import redirect
from flask import request
from hanage import Memo
from mohikan import Aso

import random
import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

haru = Flask(__name__)

@haru.route("/kobiru")
def okane():
    return render_template("kobirunope-zi.html")

@haru.route("/tyato")
def unti():
    answer=""
    return render_template("tyatonope-zi.html", random=random, answer=answer)

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


@haru.route("/ai", methods=["POST"])
def ai():
    ai=request.form.get("ai")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(ai+"。タメ口でしゃべって。")
    answer = response.text
    print(answer)
    return render_template("tyatonope-zi.html", random=random, answer=answer)

haru.run(debug=True, host="0.0.0.0")

@haru.route("/aso", methods=["GET", "POST"])
def hosi():
    kome_tati =Aso.select()
    return render_template("asobinope-zi.html",kome_tati = kome_tati)

@haru.route("/aso1", methods=["POST"])
def aso1():
    aso=request.form.get("aso")
    Aso.create(aso=aso)
    return redirect("/aso")

@haru.route("/aso_keshi/<id>", methods=["POST"])
def aso_keshi(id):
    aso = Aso.get(id=id)
    aso.delete_instance()
    return redirect("/aso")


