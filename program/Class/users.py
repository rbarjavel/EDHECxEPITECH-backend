from Class.database import Database

class User:
    def __init__(self):
        self.userDatabaseName = "users"
        self.userDatabaseMetaName = "users_metas"
        self.database = Database()

    def createUser(self, user_name, password, store_id, metas):
        elements = {
            "User_name": user_name,
            "Password": password,
            "Store" : store_id
        }
        id = self.database.createElement(elements, self.userDatabaseName)
        for info in metas:
            self.database.createMeta(info, metas[info], id, self.userDatabaseMetaName)
        return(id)