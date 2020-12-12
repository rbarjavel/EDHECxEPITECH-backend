from Class.database import Database

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
        verity = 1
        for product in products:
            for category in categories:
                if (category in product and product[category] == categories[category]):
                    pass
                else:
                    verity = 0
            if (verity == 1):
                availableProduct.append(product)
            else:
                verity = 1
        print(availableProduct)
        return (availableProduct)