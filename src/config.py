class Config:
    SECRET_KEY = 'bN12aBL345KFNC!%vhUI*S'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'sSilus50'
    MYSQL_DB = 'login-flask'     

config = {
    'development': DevelopmentConfig
}