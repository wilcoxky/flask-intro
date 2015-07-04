import unittest
from flask.ext.testing import TestCase
from flask.ext.login import current_user
from project import app, db
from project.models import BlogPosts, User


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.client = app.test_client()
        db.create_all()
        user = User("admin", "admin@in.com", "admin")
        db.session.add(user)
        db.session.add(
            BlogPosts("Test post", "This is a test. Only a test.", user.id))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure Flask set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    # Ensure Content being displayed
    def test_content_within_database(self):
        response = self.client.post(
            '/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertTrue(b'Test post' in response.data)

class UsersViewsTest(BaseTestCase):

    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Please login', response.data)

    # ensure main page requires login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertTrue(b'you must log in first!' in response.data)

    # Ensure login has the correct text
    def test_login_text(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure login benhave on correct input
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            self.assertTrue(b'You were just logged in' in response.data)
            self.assertTrue(current_user.name == 'admin' , msg=None)

    # Ensure login benhave on incorrect input
    def test_incorrect_login(self):
        with self.client:
            response = self.client.post(
                '/login', data=dict(username="asdasd", password="asdasd"), follow_redirects=True)
            self.assertTrue(
                b'Invalid Credentials. Please try again' in response.data)


    # Ensure logout
    def test_logout(self):
        with self.client:
            response = self.client.post(
                '/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            response = self.client.get('/logout', follow_redirects=True)
            self.assertTrue(b'You were just logged out' in response.data)
            self.assertFalse(current_user.is_active())


class UserRegistrationTest(BaseTestCase):
    # Ensure login benhave on correct input
    def test_register_user(self):
        with self.client:
            response = self.client.post(
                '/register', data=dict(username="test",email="test@test.com",password="test",
                confirmPassword="test"), follow_redirects=True)
            self.assertTrue(current_user.name == 'test' , msg=None)


if __name__ == '__main__':
    unittest.main()
