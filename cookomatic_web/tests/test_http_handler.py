import unittest

from flask_testing import TestCase

from cookomatic_web import http_handler


class TestHttpHandler(TestCase):
    def create_app(self):
        app = http_handler.app
        app.config['TESTING'] = True
        return app

    def test_home(self):
        self.client.get('/')
        self.assert_template_used('index.html')

    def test_404(self):
        response = self.client.get('/asdf')
        self.assert404(response)

if __name__ == '__main__':
    unittest.main()
