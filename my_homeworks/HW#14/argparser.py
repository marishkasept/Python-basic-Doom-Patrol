import argparse
import json

class DataException(Exception):
    def __init__(self, message='User with this username or email is already exist!'):
        self.message = message

    def __str__(self):
        return self.message


parser = argparse.ArgumentParser(description="Hometask parser")
parser.add_argument('-u', '--username', dest='us', type=str)
parser.add_argument('-e', '--email', dest='em', type=str)
parser.add_argument('-s', '--status', dest='st', type=bool)

args = parser.parse_args()

data = {
        "username": args.us,
        "email": args.em,
        "status": args.st
    }

with open('hw.json', 'r') as file:
    all_users = json.loads(file.read())

if len(all_users) > 0:
    for user in all_users:
        if data['username'] == user['username'] or data['email'] == user['email']:
            raise DataException()
all_users.append(data)

with open('hw.json', 'w') as file:
    file.write(json.dumps(all_users))





