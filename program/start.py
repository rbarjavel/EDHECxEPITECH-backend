import sqlite3
from Class.database import Database
from Class.datacenter import Datacenter
from Class.storage import Storage
from Class.hosting import Hosting

datacenter = Datacenter()
storage = Storage()
hosting = Hosting()
id = datacenter.createDatacenter("datacenter1", "81.89.29.21", "nice")
id = storage.createStorage("storage1", "serveur.stromfy.com", "200", id)
hosting.createHosting(id, "hosting1", "200", 1)