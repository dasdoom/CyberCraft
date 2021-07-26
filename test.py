import vcr
from unittest import TestCase
from app import app
import requests


class GitSearchTest(TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index_load(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Enter GitHub Login' in response.data)

    @vcr.use_cassette('VCR.yaml')
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(login='dasdoom'))
        self.assertIn(b'Danya', response.data)

    @vcr.use_cassette('VCR1.yaml')
    def test_correct_name_from_api(self):
        tester = app.test_client(self)
        login = 'dasdoom'
        response = tester.post('/', data=dict(login=login))
        response_rest = requests.get(f'https://api.github.com/users/{login}')
        self.assertIn(b'Danya', response.data)
        self.assertEqual('Danya', response_rest.json()['name'])

    @vcr.use_cassette('VCR2.yaml')
    def test_correct_repo_from_api(self):
        tester = app.test_client(self)
        login = 'dasdoom'
        response = tester.post('/', data=dict(login=login))
        response_rest_repo = requests.get(f'https://api.github.com/'
                                          f'users/{login}/repos')
        self.assertIn(b'epam', response.data)
        self.assertEqual('epam', response_rest_repo.json()[0]['name'])

    def test_incorrect_url(self):
        tester = app.test_client(self)
        response = tester.get('/hi')
        self.assertEqual(response.status_code, 404)

    def test_incorrect_login_enter(self):
        tester = app.test_client(self)
        login = ' '
        response = tester.post('/', data=dict(login=login))
        self.assertIn(b'Please, enter login', response.data)
