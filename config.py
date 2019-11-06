# -*- coding: UTF-8 -*-
__author__ = 'hunter'
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    app_name = "cmdb-demo"
    description = "默认环境"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    debug = False
    log_dir = "logs/"
    log_file = "info.log"
    error_log_file = "error.log"
    port = "8018"
    host = "0.0.0.0"

    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_RECYCLE = 7200

    redis_nodes = [{"host": "127.0.0.1", "port": "6379"}]
    redis_password = "123"
    REDIS_MAX_CONNECTIONS = 100

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    description = "开发环境"
    DEBUG = True
    debug = True
    SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{host}/{database}?charset={charset}".format(
        username="root",
        password="123",
        host="{}:{}".format("127.0.0.1", "3306"),
        database="my-db",
        charset="utf8mb4")


class BetaConfig(Config):
    description = "Beta环境"
    DEBUG = True
    debug = True
    SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{host}/{database}?charset={charset}".format(
        username="root",
        password="123",
        host="{}:{}".format("127.0.0.1", "3306"),
        database="my-db",
        charset="utf8mb4")


class TestingConfig(Config):
    description = "测试环境"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{host}/{database}?charset={charset}".format(
        username="root",
        password="123",
        host="{}:{}".format("127.0.0.1", "3306"),
        database="my-db",
        charset="utf8mb4")


class ProductionConfig(Config):
    description = "生产环境"
    DEBUG = False
    debug = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{host}/{database}?charset={charset}".format(
        username="root",
        password="123",
        host="{}:{}".format("127.0.0.1", "3306"),
        database="my-db",
        charset="utf8mb4")
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}


def get_config():
    env = os.getenv("simple_flask_web_env")
    if env == 'dev':
        conf_ = DevelopmentConfig
    elif env == 'beta':
        conf_ = BetaConfig
    else:
        conf_ = ProductionConfig
    return conf_


conf = get_config()
