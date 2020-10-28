from flask import request
from flask_cors import CORS

from .create_app import create_app
from .models import Users
from .db_utils import PostgreConnect

app = create_app()
CORS(app=app)
inside_data = PostgreConnect()
connect = inside_data.output()

user = Users(connect)


@app.route("/autorization", methods=["GET", "POST"])
def create_user():

    login = request.json.get("login")
    password = request.json.get("password")
    fname = request.json.get("fname")
    lname = request.json.get("lname")
    date_of_birth = str(request.json.get("date_of_birth"))

    if request.method == "POST":
        result = user.create_user(login, password, fname, lname, date_of_birth)

        return {"Response": result}

    else:
        return "This is Get request"