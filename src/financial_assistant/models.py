from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from loguru import logger

from .db_utils import PostgreHandler


class Users(object):
    def __init__(self, connect):
        self.connect = connect

    def create_user(self, login, password, fname, lname, date_of_birth):
        password_hash = generate_password_hash(password)
        date_create = str(datetime.now())
        user_data = {
            "login": login,
            "password": password_hash,
            "fname": fname,
            "lname": lname,
            "date_of_birth": date_of_birth,
            "date_create": date_create,
        }
        hand = PostgreHandler(self.connect)
        result = hand.create_user(user_data)

        return result

    def check_user(self, login, password):
        hand = PostgreHandler(self.connect)
        password_from_db = hand.check_user(login)

        if password_from_db["result"]:

            check_pass = check_password_hash(password_from_db["result"], password)
            logger.info(check_pass)

            if check_pass == True:
                return {"result": True}
            else:
                return {"result": True}

        else:
            return {"result": "Not user with so login"}
