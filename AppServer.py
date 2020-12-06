import os
import DataSource
import falcon
import json
from waitress import serve

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
searcher = DataSource.InMemorySearcher(
    os.path.join(THIS_FOLDER, "products.json"))


class CategoryResource:
    def on_get(self, req, resp, **kwargs):

        category = ''
        keyword = ''

        if 'category' in kwargs:
            category = kwargs['category'].lower()
        if 'word' in kwargs:
            keyword = kwargs['word'].lower()

        resp.content_type = falcon.MEDIA_JSON

        try:
            if category == '' and keyword == '':
                resp.body = '{"categories": ' + \
                    json.dumps(searcher.get_categories()) + "}"
            else:
                if category != '' and keyword == '':
                    matching_products = searcher.get_products(category)
                else:
                    matching_products = searcher.get_products(
                        category, keyword)

                resp.body = '{"products": [' + \
                    ", ".join([product.toJson()
                               for product in matching_products]) + "]}"
        except Exception as ex:
            print("Error in CategoryResource. Category='%s', keyword='%s'. Error: %s" %
                  (category, keyword, ex))
            raise falcon.HTTPInternalServerError('Internal Error')


class KeywordResource:
    def on_get(self, req, resp, **kwargs):
        keyword = ''
        if 'word' in kwargs:
            keyword = kwargs['word'].lower()

        resp.content_type = falcon.MEDIA_JSON

        try:
            if(keyword == ''):
                resp.body = '{"keywords": ' + \
                    json.dumps(searcher.get_keywords()) + "}"
            else:
                resp.body = '{"products": [' + \
                    ", ".join([product.toJson()
                               for product in searcher.get_products('', keyword)]) + "]}"
        except Exception as ex:
            print("Error in KeywordResource. Keyword='%s'. Error: %s" %
                  (keyword, ex))
            raise falcon.HTTPInternalServerError('Internal Error')


app = falcon.API()
categories_resource = CategoryResource()
keyword_resouce = KeywordResource()

app.add_route('/search/category', categories_resource)
app.add_route('/search/category/{category}', categories_resource)
app.add_route(
    '/search/category/{category}/keyword/{word}', categories_resource)
app.add_route('/search/keyword', keyword_resouce)
app.add_route('/search/keyword/{word}', keyword_resouce)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
