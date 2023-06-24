from urllib.parse import quote_plus
import os
import logging

class Config(object):
    DEBUG = False
    user = ""
    password = ""
    host = ""
    port = ""
    dbname = ""
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{quote_plus(password)}@{host}:{port}/{dbname}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

class DevConfig(object):
    DEBUG = True
    user = os.getenv('SQLUSER')
    password = os.getenv('SQLPASS')
    host = "localhost"
    port = "3306"
    dbname = "fisky"
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{quote_plus(password)}@{host}:{port}/{dbname}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    REDIS_URL = "redis://:@localhost:6379/0"

    # print(SQLALCHEMY_DATABASE_URI)

weixin = {
    "appid":os.getenv('wxappid'),
    "secret":os.getenv('wxsecret')

}


if __name__ == "__main__":
    dev = DevConfig()
    print(dev.SQLALCHEMY_DATABASE_URI)