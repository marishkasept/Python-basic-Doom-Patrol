import pytest
import os
import shutil
import json
from config import Config
from unittest.mock import patch
import user_functions as uf

TEST_ALL_USERS_DATA = [{"first_name": "test", "last_name": "test", "Email": "test@test.com", "id": 1}, {"first_name": "test1", "last_name": "test1", "Email": "test1@test.com", "id": 2}]
TEST_EMAIL = "test@test.com"
TEST_FALSE_EMAIL = "sobaka@sobaka.com"
TEST_DATABASE_DIRECTORY = 'test_database'
TEST_FILE = 'test.json'
TEST_FILE_PATH = TEST_DATABASE_DIRECTORY + "/" + TEST_FILE
TEST_INPUT = "hello"
TEST_INPUT_UPDATE = 1

def setup():
    if os.path.exists(TEST_DATABASE_DIRECTORY):
        shutil.rmtree(TEST_DATABASE_DIRECTORY)
    Config.USERS_DIRECTORY = TEST_DATABASE_DIRECTORY
    Config.USERS_FILE = TEST_FILE
    Config.PATH_TO_USERS_FILE = TEST_FILE_PATH

def test_check_email():
    assert uf.check_email(TEST_EMAIL, TEST_ALL_USERS_DATA) == True
    assert uf.check_email(TEST_FALSE_EMAIL, TEST_ALL_USERS_DATA) == False

def test_create_file():
    file = uf.create_file()
    assert os.path.exists(TEST_DATABASE_DIRECTORY) == True
    assert os.path.exists(Config.PATH_TO_USERS_FILE) == True
    data = json.loads(file.read())
    assert (type(data) is list) == True
    file.close()
    shutil.rmtree(TEST_DATABASE_DIRECTORY)

@patch('user_functions.input')
def test_user_add(input_mock):
    file = uf.create_file()
    input_mock.return_value = TEST_INPUT
    uf.user_add()
    data = json.loads(file.read())
    file.close()
    assert (len(data) > 0) == True
    assert data[0]['first_name'] == TEST_INPUT
    assert data[0]['id'] == 1
    shutil.rmtree(TEST_DATABASE_DIRECTORY)

@patch('user_functions.input')
def test_update_user(input_mock):
    file = uf.create_file()
    file.close()
    input_mock.return_value = TEST_INPUT
    uf.user_add()
    input_mock.return_value = TEST_INPUT_UPDATE
    uf.update_user()
    file = open(Config.PATH_TO_USERS_FILE, 'r')
    data = json.loads(file.read())
    file.close()
    assert data[0]['first_name'] == TEST_INPUT_UPDATE
    assert data[0]['last_name'] == TEST_INPUT_UPDATE
    assert data[0]['Email'] == TEST_INPUT_UPDATE
    shutil.rmtree(TEST_DATABASE_DIRECTORY)
