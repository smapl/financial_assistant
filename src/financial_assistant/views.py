from flask import request, render_template, session, redirect, url_for
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


@app.route("/personality", methods=["GET"])
@cross_origin()
def personality():
    if "user_name" in session:
        return render_template("main.html")
    else:
        return "Not login"


@app.route("/identification/registration", methods=["POST", "GET"])
@cross_origin()
def create_user():
    if request.method == "GET":
        return "this get resquest (registration)"

    login = request.json.get("login")
    password = request.json.get("password")
    fname = request.json.get("fname")
    lname = request.json.get("lname")
    email = request.json.get("email")
    date_of_birth = str(request.json.get("date_of_birth"))

    if request.method == "POST":
        result = user.create_user(login, password, fname, lname, date_of_birth, email)

        return {"Response": result}

    else:
        return "This is Get request"


@app.route("/identification/login", methods=["POST", "GET"])
@cross_origin()
def check_user():
    if request.method == "GET":
        return "this get resquest (login)"

    if request.method == "POST":
        login = request.json.get("login")
        password = request.json.get("password")
        db_res = user.check_user(login, password)

        logger.info(db_res["result"])
        if db_res["result"] == True:
            session["user_name"] = login
            logger.info(session["user_name"])

        return db_res
