from Class.database import Database

class Hosting:
    def __init__(self):
        self.hostingDatabaseName = "hostings"
        self.hostingDatabaseMetaName = "hostings_metas"
        self.database = Database()


    def createHosting(self, storage_id, name, size, user_id):
        elements = {
            "Storage_id": str(storage_id),
            "Hosting_name": name,
            "Hosting_size" : size,
            "User_id" : str(user_id)
        }
        id = self.database.createElement(elements, self.hostingDatabaseName)
        self.createBasicMetas(id)
        return(id)
    
    def createBasicMetas(self, parent_id):
        self.database.createMeta("Free_space", "100%", parent_id, self.hostingDatabaseMetaName)