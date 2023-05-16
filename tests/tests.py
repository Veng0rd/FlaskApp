import unittest

from flask import current_app
from flask_login import login_user
from werkzeug.security import generate_password_hash

from app import create_app, db
from app.models import User
from config import TestingConfig


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()  # создает контекст приложения Flask для каждого теста
        self.app_context.push()  # активирует контекст приложения Flask
        db.create_all()

    def tearDown(self):
        """ Вызывается после каждого теста, чтобы удалить таблицы базы данных и закрыть контекст приложения"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        """ Существует ли приложение """
        self.assertFalse(current_app is None)

    def test_root(self):
        """ Подключается ли  """
        response = self.app.test_client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        """ Создается ли user """
        new_user = User(email='test@example.com', login='testuser', password='password')
        db.session.add(new_user)
        db.session.commit()
        found_user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.login, 'testuser')
        self.assertEqual(found_user.password, 'password')

    def test_app_is_testing(self):
        """ В тестовом ли режиме приложение """
        self.assertTrue(current_app.config['TESTING'])

    def test_signup_post_response(self):
        response = self.app.test_client().post('/signup', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_post_response(self):
        response = self.app.test_client().post('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # def test_root_profile(self):
    #     with self.app.test_request_context('/login'):
    #         new_user = User(id="1", email='test@example.com', login='testuser', password='password')
    #         db.session.add(new_user)
    #         db.session.commit()
    #         found_user = User.query.filter_by(email='test@example.com').first()
    #
    #         with self.app.test_client().session_transaction() as session:
    #             session['id'] = found_user.id
    #
    #         with self.app.test_request_context('/profile', method='POST'):
    #             response = self.app.test_client().post('/profile', follow_redirects=True)
    #             self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
