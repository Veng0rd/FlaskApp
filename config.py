import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'database.db').replace('\\', '/')
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_ERROR_MESSAGES = {'missing-input-response': 'Please complete the captcha'}


class DevelopmentConfig(Config, object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'app/database.db').replace('\\', '/')
    DEBUG = True
    TESTING = True



class TestingConfig(Config, object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'database.db').replace('\\', '/')
    DEBUG = True
    TESTING = True
