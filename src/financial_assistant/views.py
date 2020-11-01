from flask import Flask, request, redirect, url_for, render_template
from flask_cors import CORS, cross_origin

from .create_app import create_app


app = create_app()
CORS(app)


@app.route("/", methods=["GET"])
@cross_origin()
def begin():
    return render_template("index.html")


@app.route("/main", methods=["POST"])
@cross_origin()
def main():
    resp = request.json.get("transp")
    print(resp)
    if resp == True:
        return redirect(url_for("other"))
    else:
        return "error"


@app.route("/other")
@cross_origin()
def other():
    return render_template("main.html")
