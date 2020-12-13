from Class.database import Database

class Datacenter:
    def __init__(self):
        self.datacentersDatabaseName = "datacenters"
        self.datacentersDatabaseMetaName = "datacenters_metas"
        self.database = Database()


    def createDatacenter(self, name, host, city):
        elements = {
            "Datacenter_name": name,
            "Datacenter_host": host,
            "Datacenter_city" : city
        }
        id = self.database.createElement(elements, self.datacentersDatabaseName)
        self.createBasicMetas(id)
        return(id)
    
    def createBasicMetas(self, parent_id):
        self.database.createMeta("Status", "down", parent_id, self.datacentersDatabaseMetaName)