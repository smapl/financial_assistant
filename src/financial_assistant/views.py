from flask import request, render_template, session, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin

from loguru import logger


from .create_app import create_app
from .models import Users
from .db_utils import PostgreConnect

app = create_app()
CORS(app=app)
inside_data = PostgreConnect()
connect = inside_data.output()

user = Users(connect)


@app.route("/identification", methods=["GET"])
@cross_origin()
def begin_page():
    return render_template("index.html")


@app.route("/", methods=["GET"])
@cross_origin()
def personality():
    if "user_name" in session:
        return render_template("profile.html")
    else:
        return render_template("index.html")


@app.route("/identification/registration", methods=["POST", "GET"])
@cross_origin()
def create_user():
    if request.method == "GET":
        return "this get resquest (registration)"
    logger.info(request.data)
    login = request.json.get("login")
    password = request.json.get("password")
    fname = request.json.get("fname")
    lname = request.json.get("lname")
    email = request.json.get("email")
    date_of_birth = str(request.json.get("date_of_birth"))

    result = user.create_user(login, password, fname, lname, date_of_birth, email)

    return result


@app.route("/identification/login", methods=["POST", "GET"])
@cross_origin()
def check_user():
    logger.info(request.data)
    if request.is_json == False:
        return {"result": "error params type"}
    if request.method == "GET":
        return "this get resquest (login)"

    if request.method == "POST":
        login = request.json.get("login")
        password = request.json.get("password")
        db_res = user.check_user(login, password)

        if db_res["result"] == True:
            session["user_name"] = login
            output_data = {
                "result": True,
                "redirect_url": "http://0.0.0.0:5000/",
            }
            logger.info(output_data)

            return jsonify(output_data)

        return jsonify(db_res)


@app.route("/personality/indent_user", methods=["GET"])
@cross_origin()
def indent_user():
    logger.info(session["user_name"])
    return jsonify({"user_name": session["user_name"]})
