import json

USER_FILE = "users.json"
MEMBER_FILE = "members.json"


def load_users():
    try:
        file = open(USER_FILE, "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return []


def save_users(users):
    file = open(USER_FILE, "w")
    json.dump(users, file)
    file.close()


def load_members():
    try:
        file = open(MEMBER_FILE, "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return []

def save_members(members):
    file = open(MEMBER_FILE, "w")
    json.dump(members, file)
    file.close()
