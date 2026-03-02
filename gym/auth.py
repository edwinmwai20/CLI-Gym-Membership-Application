from .storage import load_users
from .models import Admin, Staff

def login():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            if user["role"] == "admin":
                return Admin(username, password)
            else:
                return Staff(username, password)

    print("Login failed.")
    return None