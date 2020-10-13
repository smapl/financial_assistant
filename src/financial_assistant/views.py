from flask import request

from .create_app import create_app
from .models import Users

app = create_app()
user = Users()


@app.route("/", methods=["GET", "POST"])
def create_user():
    login = request.json.get("login")
    password = request.json.get("password")

    if request.method == "POST":
        result = user.create_user(login, password)

        return {"result": result}

    else:
        return "This is Get request"