import unittest
import os
import shutil
import json
from config import Config
from unittest.mock import patch
from user_functions import check_email, create_file, user_add, update_user

TEST_ALL_USERS_DATA = [{"first_name": "test", "last_name": "test", "Email": "test@test.com", "id": 1}, {"first_name": "test1", "last_name": "test1", "Email": "test1@test.com", "id": 2}]
TEST_EMAIL = "test@test.com"
TEST_FALSE_EMAIL = "sobaka@sobaka.com"
TEST_DATABASE_DIRECTORY = 'test_database'
TEST_FILE = 'test.json'
TEST_FILE_PATH = TEST_DATABASE_DIRECTORY + "/" + TEST_FILE
TEST_INPUT = "hello"
TEST_INPUT_UPDATE = 1

class TestUserFunctions(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TEST_DATABASE_DIRECTORY):
            shutil.rmtree(TEST_DATABASE_DIRECTORY)
        Config.USERS_DIRECTORY = TEST_DATABASE_DIRECTORY
        Config.USERS_FILE = TEST_FILE
        Config.PATH_TO_USERS_FILE = TEST_FILE_PATH

    def test_check_email(self):
        self.assertTrue(check_email(TEST_EMAIL, TEST_ALL_USERS_DATA))
        self.assertFalse(check_email(TEST_FALSE_EMAIL, TEST_ALL_USERS_DATA))

    def test_create_file(self):
        file = create_file()
        self.assertTrue(os.path.exists(TEST_DATABASE_DIRECTORY))
        self.assertTrue(os.path.exists(Config.PATH_TO_USERS_FILE))
        data = json.loads(file.read())
        self.assertTrue(type(data) is list)
        file.close()
        shutil.rmtree(TEST_DATABASE_DIRECTORY)

    @patch('user_functions.input')
    def test_user_add(self, input_mock):
        file = create_file()
        input_mock.return_value = TEST_INPUT
        user_add()
        data = json.loads(file.read())
        file.close()
        self.assertTrue(len(data) > 0)
        self.assertEqual(data[0]['first_name'], TEST_INPUT)
        self.assertEqual(data[0]['id'], 1)
        shutil.rmtree(TEST_DATABASE_DIRECTORY)

    @patch('user_functions.input')
    def test_update_user(self, input_mock):
        file = create_file()
        file.close()
        input_mock.return_value = TEST_INPUT
        user_add()
        input_mock.return_value = TEST_INPUT_UPDATE
        update_user()
        file = open(Config.PATH_TO_USERS_FILE, 'r')
        data = json.loads(file.read())
        file.close()
        self.assertEqual(data[0]['first_name'], TEST_INPUT_UPDATE)
        self.assertEqual(data[0]['last_name'], TEST_INPUT_UPDATE)
        self.assertEqual(data[0]['Email'], TEST_INPUT_UPDATE)
        shutil.rmtree(TEST_DATABASE_DIRECTORY)
