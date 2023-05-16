from app import create_app
from flask_script import Manager
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)
manager = Manager(app)

if __name__ == '__main__':
    app.run()