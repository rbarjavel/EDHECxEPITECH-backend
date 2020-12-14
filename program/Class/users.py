from Class.database import Database
from Class.stores import Store

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

        stores = self.database.getAllElements("stores")
        for store in stores:
            if (store_id == store["Store_name"]):
                elements["Store"] = store["id"]
                id = self.database.createElement(elements, self.userDatabaseName)

                for info in metas:
                    self.database.createMeta(info, metas[info], id, self.userDatabaseMetaName)
                return(id)

        return (-84)

    def login(self, user_name, password):
        users = self.database.getAllElements(self.userDatabaseName)

        for user in users:
            if (user["User_name"] == user_name and
                user["Password"] == password):

                store = Store()
                stores_name = store.getElement(user["Store"])

                if (stores_name == "error"):
                    return ("error")
                
                value = dict()
                value["Store_name"] = stores_name
                value["Store"] = user["Store"]

                return (value)

        return ("error")
