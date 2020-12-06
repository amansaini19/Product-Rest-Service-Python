import json
from Product import Product


def load_json(file):
    print("Started reading file: " + file)

    with open(file, "r") as read_file:
        data = json.load(read_file)

    print("Done reading file")

    products = []
    for entry in data["products"]:
        products.append(Product(**entry))

    return products


class InMemorySearcher:

    def __init__(self, file):
        self.file = file
        self.products = load_json(file)
        self.keyword_products = self.get_keyword_to_products_dict()

    def get_categories(self):
        """ Return a list of unique categories """

        return list(set([product.category for product in self.products]))

    def get_products(self, category='', keyword=''):
        """ Return a list of products matching the category, keyword or 
            (category and keyword)"""

        if category != '':
            products_matching_categories = [
                product for product in self.products if product.category.lower() == category]

            if keyword == '':
                return products_matching_categories
            else:
                return [product for product in products_matching_categories
                        if keyword in product.keywords]
        else:
            return self.keyword_products[keyword]

    def get_keywords(self):
        """Return a list of all known keywords"""

        return list(self.keyword_products.keys())

    def get_keyword_to_products_dict(self):
        """Return a dictionary of all product keywords as keys with a list of products as values"""

        keyword_products = {}
        for product in self.products:
            for keyword in product.keywords:
                if keyword in keyword_products:
                    products_list = keyword_products[keyword]
                else:
                    products_list = []

                products_list.append(product)
                keyword_products[keyword] = products_list

        return keyword_products
