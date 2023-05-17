import unittest

from bs4 import BeautifulSoup
from flask import current_app

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
        """ Проверка POST запроса к /signup """
        response = self.app.test_client().post('/signup', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_post_response(self):
        """ Проверка POST запроса к /login """
        response = self.app.test_client().post('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_profile_get_response(self):
        """ Проверка GET запроса к /profile """
        response = self.app.test_client().get('/profile')
        self.assertNotEqual(response.status_code, 200)

    def login(self, email, password):
        return self.app.test_client().post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def signup(self, login, email, password):
        return self.app.test_client().post('/signup', data=dict(
            login=login,
            email=email,
            password=password,
            password_reply=password
        ), follow_redirects=True)

    def test_login_wrong_format(self):
        """ Проверка работы email формы на /login """
        res = self.login('random_mail', 'randompassword')
        soup = BeautifulSoup(res.data, 'html.parser')
        block = soup.find('p', class_="help-block")
        self.assertEqual(block.text, 'Неправильный формат!')

    def test_signup_wrong_format(self):
        """ Проверка работы email формы на /signup """
        res = self.signup('randomlogin', 'mail@mailcom', 'password')
        soup = BeautifulSoup(res.data, 'html.parser')
        block = soup.find('p', class_="help-block")
        self.assertEqual(block.text, 'Неправильный формат!')


if __name__ == '__main__':
    unittest.main()
