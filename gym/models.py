class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password
        self.role = role

    def check_password(self, password):
        return self.__password == password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

class Staff(User):
    def __init__(self, username, password):
        super().__init__(username, password, "staff")

class Member:
    def __init__(self, member_id, name, plan, status):
        self.id = member_id
        self.name = name
        self.plan = plan
        self.status = status