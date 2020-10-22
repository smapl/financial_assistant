import time

import psycopg2
from loguru import logger

from .utils import parse_args


postgre_login, postgre_password, host, dbname = parse_args()


class PostgreHandler(object):
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