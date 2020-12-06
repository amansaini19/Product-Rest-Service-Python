import json


class Product:

    def __init__(self, createdDate, imageUrl, title, category, isActive,
                 itemId, parentCategory, department, upc, brand, modifiedDate,
                 itemHashint64):
        self.createdDate = createdDate
        self.imageUrl = imageUrl
        self.title = title
        self.category = category
        self.isActive = isActive
        self.itemId = itemId
        self.parentCategory = parentCategory
        self.department = department
        self.upc = upc
        self.brand = brand
        self.modifiedDate = modifiedDate
        self.itemHashint64 = itemHashint64
        self.keywords = title.lower().split()
        self.toJson()

    def __str__(self):
        return "Product: %s, %s" % (self.title, self.category)

    def toJson(self):
        copy = self.__dict__.copy()
        del copy['keywords']
        return json.dumps(copy)
