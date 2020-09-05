import unittest
import sys
sys.path.append('./src/main')
from . import app

class TestResponse(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_flask_message(self):
        result = self.app.get('/')
        assert b"Server is Active!" == result.data


if __name__ == '__main__':
    unittest.main()
