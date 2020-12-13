from Class.database import Database

class Store:
    def __init__(self):
        self.storeDatabaseName = "stores"
        self.storeDatabaseMetaName = "stores_metas"
        self.database = Database()

    def createStore(self, store_name, metas):
        elements = {
            "Store_name": store_name
        }
        id = self.database.createElement(elements, self.storeDatabaseName)
        for info in metas:
            self.database.createMeta(info, metas[info], id, self.storeDatabaseMetaName)
        return(id)