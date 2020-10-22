from datetime import datetime

from werkzeug.security import generate_password_hash

from .db_utils import PostgreHandler


class Users(object):
    def __init__(self):
        self.m_handler = PostgreHandler()

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

        return
