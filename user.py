


class User:

    def __init__(self, userName, password,role):
        self.userName = userName
        self.password = password
        self.role=role
    def getUserName(self):
        return self.userName
    def getPassword(self):
        return self.password
    def getRole(self):
        return self.role

