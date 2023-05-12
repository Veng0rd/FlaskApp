import os
from dotenv import load_dotenv

load_dotenv('app/.env')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///F:/Файлики/ОПД/FlaskApp/app/db/users.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'app/db/users.db').replace('\\', '/')
