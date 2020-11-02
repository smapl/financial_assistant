from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin

from .create_app import create_app

app = create_app()
CORS(app)


@app.route("/", methods=["GET", "POST"])
@cross_origin()
def start_page():
    return render_template("start.html")


@app.route("/page_one", methods=["GET"])
@cross_origin()
def page_one():
    return render_template("page.html")


@app.route("/handler", methods=["POST"])
@cross_origin()
def handler():
    print(request.json)
    if request.json.get("module") == True:
        return "http://0.0.0.0:5000/page_one"
    return "error"