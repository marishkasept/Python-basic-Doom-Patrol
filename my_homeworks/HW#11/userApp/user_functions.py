import json
import os
import logging
from config import Config

def check_email(email, all_users_data):
    for user in all_users_data:
        if email == user['Email']:
            return True
    return False

def create_file():
    if os.path.exists(Config.USERS_DIRECTORY) == False:
        os.mkdir(Config.USERS_DIRECTORY)
    file = open(Config.PATH_TO_USERS_FILE, 'w')
    file.write(json.dumps([]))
    file.close()
    return open(Config.PATH_TO_USERS_FILE, 'r')


def user_add():
    user = {
        "first_name": input("First Name: "),
        "last_name": input("Last Name: "),
        "Email": input("Email: "),
    }
    try:
        file = open(Config.PATH_TO_USERS_FILE, 'r')
    except FileNotFoundError:
        logging.critical("File Not Found Error!!!")
        file = create_file()
    all_users_data_json = file.read()
    all_users_data = json.loads(all_users_data_json)
    file.close()
    if len(all_users_data) > 0:
        user['id'] = all_users_data[-1]['id'] + 1
    else:
        user['id'] = 1
    if check_email(user['Email'], all_users_data) == False:
        all_users_data.append(user)
        with open(Config.PATH_TO_USERS_FILE, 'w') as file:
            file.write(json.dumps(all_users_data))
    else:
        print("User with this email already exist!!!")


def get_all():
    with open(Config.PATH_TO_USERS_FILE, 'r') as file:
        users = json.loads(file.read())
        for user in users:
            print("User #" + str(user['id']))
            print("First Name: " + user['first_name'])
            print("Last Name: " + user['last_name'])
            print("Email: " + user['Email'])


def search_by(search_str, what_to_search):
    if what_to_search in Config.FIELDS_OF_USER:
        with open(Config.PATH_TO_USERS_FILE, 'r') as file:
            users = json.loads(file.read())
            for user in users:
                if str(user[what_to_search]).lower() == str(search_str).lower():
                    print("User #" + str(user['id']))
                    print("First Name: " + user['first_name'])
                    print("Last Name: " + user['last_name'])
                    print("Email: " + user['Email'])
    else:
        logger.warning("User trying to search query which not in fields list")
        print("You want to search by field which not in user fields!!!")


def update_user():
    file = open(Config.PATH_TO_USERS_FILE, 'r')
    users = json.loads(file.read())
    file.close()
    id = int(input("Type id of user which you want to update: "))
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    for user in users:
        if user['id'] == id:
            user['first_name'] = first_name
            user['last_name'] = last_name
            user['Email'] = email
    with open(Config.PATH_TO_USERS_FILE, 'w') as file:
        file.write(json.dumps(users))