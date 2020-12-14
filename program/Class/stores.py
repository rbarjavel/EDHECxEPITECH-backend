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

    def getElement(self, store_id):
        stores = self.database.getAllElements(self.storeDatabaseName)

        id = int(store_id)
        for store in stores:
            if (store["id"] == id):
                return (store["Store_name"])

        return ("error")