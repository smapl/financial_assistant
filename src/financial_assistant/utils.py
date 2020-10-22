import argparse


def parse_args() -> tuple:
    parser = argparse.ArgumentParser(description="Ping script")

    parser.add_argument("--login", action="store", dest="login")
    parser.add_argument("--password", action="store", dest="password")
    parser.add_argument("--host", action="store", dest="host")
    parser.add_argument("--db_name", action="store", dest="db_name")

    args = parser.parse_args()

    postgre_login = args.login
    postgre_password = args.password
    host = args.host
    db_name = args.db_name

    return postgre_login, postgre_password, host, db_name
