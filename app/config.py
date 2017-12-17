import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    SECRET_KEY = "fdshfgdsagfdshgshgf"
    path = "sqlite:///{}\\test2.sqlite".format(basedir)
    SQLALCHEMY_DATABASE_URI =path
    #SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_migrate')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
class ProductionConfig(Config):
    DEBUG=False
class DevelopConfig(Config):
    DEBUG=True
