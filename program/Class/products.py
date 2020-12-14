from Class.database import Database
from Class.stores import Store

def funVer(e):
    return e["Ver"]

class Product:
    def __init__(self):
        self.productDatabaseName = "products"
        self.productDatabaseMetaName = "products_metas"
        self.database = Database()

    def createProduct(self, store_id, product_name, metas):
        elements = {
            "Store_id": store_id,
            "Product_name": product_name
        }
        id = self.database.createElement(elements, self.productDatabaseName)
        for info in metas:
            self.database.createMeta(info, metas[info], id, self.productDatabaseMetaName)
        return(id)
    
    def getProduct(self):
        products = self.database.getAllElements(self.productDatabaseName)
        for product in products:
            product_metas = self.database.getAllMetaElements(self.productDatabaseMetaName, product["id"])
            for product_meta in product_metas:
                product[product_meta["Meta_key"]] = product_meta["Meta_value"]
        return(products)
    
    def sortProduct(self, categories):
        availableProduct = []
        products = self.getProduct()
        store = Store()

        for product in products:
            key = product.items() & categories.items()
            if (key):
                product["Ver"] = len(key)
                
                product["Store_name"] = store.getElement(product["Store_id"])

                availableProduct.append(product)
        print(availableProduct)

        availableProduct.sort(key=funVer, reverse=True)

        return (availableProduct)