from flask import request
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


@app.route("/registration", methods=["POST"])
@cross_origin()
def create_user():
    print(request.data)
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


@app.route("/login", methods=["POST"])
@cross_origin()
def check_user():
    print(request.data)
    if request.method == "POST":
        login = request.json.get("login")
        password = request.json.get("password")
        db_res = user.check_user(login, password)
        return db_res