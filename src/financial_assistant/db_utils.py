import time

import psycopg2
from loguru import logger

from .utils import parse_args


postgre_login, postgre_password, host, dbname = parse_args()


class PostgreConnect(object):
    def __init__(self):
        while True:
            try:
                self.connection = psycopg2.connect(
                    dbname=dbname,
                    user=postgre_login,
                    password=postgre_password,
                    host=host,
                )
                break

            except Exception as ex:
                logger.error(ex)

                logger.info("attempt to reconnect after 10 seconds")
                time.sleep(10)

    def output(self):
        return self.connection


class PostgreHandler(object):
    def __init__(self, connect):
        self.connect = connect

    def create_user(self, data: dict):
        cursor = self.connect.cursor()
        try:

            rows = ""
            values = ""
            for row in data:
                rows += f"{row},"
                values += f"'{data[row]}',"

            rows = rows[:-1]
            values = values[:-1]

            cursor.execute(
                f"""
                INSERT INTO users 
                ({rows})
                VALUES ({values});
            """
            )
            self.connect.commit()
            return {"result": "success"}

        except Exception as ex:
            logger.error(ex)
            return {"result": ex}
