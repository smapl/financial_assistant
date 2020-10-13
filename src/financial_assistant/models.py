from werkzeug.security import generate_password_hash

from .db_utils import MongoHandler


class Users(object):
    def __init__(self):
        self.m_handler = MongoHandler()

    def create_user(self, login, password):
        password_hash = generate_password_hash(password)
        user_data = {"User_login": login, "User_password": password_hash}
        result = self.m_handler.insert_to_mongo(user_data)

        return result