import mariadb
import time
import json

class Database:
    def __init__(self):
        self.connect()
        print(__class__.__name__ + ": successfull connected to database")
        self.cursor = self.conn.cursor(dictionary=True)
        self.initTables()
    
    def initTables(self):
        self.datacentersDatabaseName = "datacenters"
        self.storageDatabaseName = "storages"
        self.hostingDatabaseName = "hostings"
        self.datacentersDatabaseMetaName = "datacenters_metas"
        self.storageDatabaseMetaName = "storages_metas"
        self.hostingDatabaseMetaName = "hostings_metas"
        self.createtable(self.datacentersDatabaseName)
        self.createtable(self.storageDatabaseName)
        self.createtable(self.hostingDatabaseName)
        self.createtable(self.datacentersDatabaseMetaName)
        self.createtable(self.storageDatabaseMetaName)
        self.createtable(self.hostingDatabaseMetaName)

    def createElement(self, elements, tableName):
        keys = "("
        values = "("
        i = 0
        for element in elements:
            keys = keys + element
            values = values + '%(' + element + ')s'
            i = i +1
            if (i < len(elements)):
                keys = keys + ', '
                values = values + ', '
        keys = keys + ')'
        values = values + ')'
        command = "INSERT INTO " + tableName + " " + keys + " " + "VALUES " + values
        print(command)
        self.cursor.execute(command, elements)
        self.conn.commit()
        return (self.cursor.lastrowid)

    def createMeta(self, meta_key, meta_value, parent_id, tableName):
        elements = {
            "Meta_key": meta_key,
            "Meta_value": meta_value,
            "Parent_id" : str(parent_id)
        }
        self.createElement(elements, tableName)

    def modifyMeta(self, parent_id, key, value, tableName):
        command = "UPDATE " + tableName + " SET Meta_value = '" + value + "' WHERE Meta_key = '" + key + "' AND Parent_id =" + str(parent_id)
        self.cursor.execute(command)
        self.conn.commit()

    def readConf(self, tableName):
        path = "./program/Config/Database/"
        with open(path + tableName + ".json") as json_file:
            data = json.load(json_file)
        return(data)

    def createtable(self, tableName):
        elements = self.readConf(tableName)
        command = "CREATE TABLE IF NOT EXISTS " + tableName + " (id INT AUTO_INCREMENT PRIMARY KEY"
        for element in elements:
            command = command + ", " + element['Name'] + " " + element['Type']
        self.cursor.execute(command + ")")

    def getElements(self, tableName, id):
        command = "SELECT * FROM "  + tableName +  " WHERE id =" + str(id)
        self.cursor.execute(command)
        return(self.cursor.fetchone())

    def getMetaElements(self, tableName, id, meta_key):
        command = "SELECT * FROM "  + tableName +  " WHERE Parent_id =" + str(id) + " AND Meta_key ='" + meta_key + "'"
        self.cursor.execute(command)
        return(self.cursor.fetchone())

    def connect(self):
        while(1):
            try:
                self.conn = mariadb.connect(
                    host='db',
                    port=3306,
                    user='root',
                    password='Test1234',
                    database='hosting'
                )
                break
            except:
                print(__class__.__name__ + ": failed to connect to database")