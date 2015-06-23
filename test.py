from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    #Ensure Flask set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    #Ensure login has the correct text
    def test_login_text(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertTrue(b'Please login' in response.data)

    #Ensure login benhave on correct input
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username = "admin", password = "admin")
        ,follow_redirects = True)
        self.assertTrue(b'You were just logged in' in response.data)


    #Ensure login benhave on incorrect input
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username = "asdasd", password = "asdasd")
        ,follow_redirects = True)
        self.assertTrue(b'Invalid Credentials. Please try again' in response.data)

    #Ensure logout
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username = "admin", password = "admin")
        ,follow_redirects = True)
        response = tester.get('/logout' ,follow_redirects = True)
        self.assertTrue(b'You were just logged out' in response.data)

    #ensure main page requires login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/' ,follow_redirects = True)
        self.assertTrue(b'you must log in first!' in response.data)



if __name__ == '__main__':
    unittest.main()
