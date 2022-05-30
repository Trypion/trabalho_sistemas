# FAKE DATABASE
USERS = [
    {
        "login": "admin",
        "password": "d033e22ae348aeb5660fc2140aec35850c4da997",
        "role": "admin",
    },
    {
        "login": "user",
        "password": "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d",
        "role": "user",
    }

]


class DatabaseConnection():
    def __init__(self, options = None):
        self.options = options
        self.connection = None

    def findUserByLogin(self, login):
        for user in USERS:
            if user["login"] == login:
                return user
        return None
