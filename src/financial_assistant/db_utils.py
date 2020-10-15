from pymongo import MongoClient
from loguru import logger


class MongoHandler(object):
    def __init__(self):
        while True:
            try:
                client = MongoClient()
                database = client["financial_assistant"]
                self.collection_users = database["Users"]
                break

            except Exception as ex:
                logger.error(ex)

    def insert_to_mongo(self, request):
        try:
            self.collection_users.insert_one(request)
            return {"Request": "Success"}

        except Exception as ex:
            logger.error(ex)
            return {"Request": "Error"}

    def get_by_mongo_users(self):
        result = []
        for doc in self.collection_users({}):
            result.append(doc)

        return result