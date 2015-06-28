# default config
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\x98m!Z\x18-\x8a\xb5N(\xcd\xed\xa8K\xbb\xaf\xbd0\xe7\xc9\x1b\xf3&\x92'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
