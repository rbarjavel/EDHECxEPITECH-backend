from Class.database import Database

class Storage:
    def __init__(self):
        self.storageDatabaseName = "storages"
        self.storageDatabaseMetaName = "storages_metas"
        self.database = Database()


    def createStorage(self, name, domain, size, datacenter_id):
        elements = {
            "Storage_name": name,
            "Datacenter_id": str(datacenter_id),
            "Storage_domain" : domain,
            "Storage_size" : size
        }
        id = self.database.createElement(elements, self.storageDatabaseName)
        self.createBasicMetas(id)
        return(id)
    
    def createBasicMetas(self, parent_id):
        self.database.createMeta("Status", "down", parent_id, self.storageDatabaseMetaName)
        self.database.createMeta("Free_space", "100%", parent_id, self.storageDatabaseMetaName)
