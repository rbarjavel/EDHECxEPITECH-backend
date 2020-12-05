import sqlite3
from Class.database import Database
from Class.users import User
from Class.products import Product
from Class.stores import Store

database = Database()
store = Store()
user = User()
stores_infos = {
    "store_img_url": "https://i2-prod.essexlive.news/whats-on/shopping/article510797.ece/ALTERNATES/s1200b/primark-2.jpg",
    "store_contact": "0498989876"
}

id = store.createStore("primemark", stores_infos)

infos = {
        "Store": "primark",
        "Nom" : "test",
        "Prénom": "test",
        "Poste":"manager"
    }
user.createUser("kelian", "bailet", id, infos)

product = Product()

infos = {
        "Couleur": "rouge, bleu",
        "Taille" : "s",
        "tissu": "coton",
    }

product.createProduct(id, "chemise lacoste", infos)
product.createProduct(id, "chemise roya", infos)
product.createProduct(id, "chemise acola", infos)

product.getProduct()