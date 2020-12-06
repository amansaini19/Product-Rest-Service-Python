# Product-Rest-Service-Python

This is a Python implementation of the Java project https://github.com/amansaini19/Product-Rest-Service

Please note that this is my first ever Python application. I read a Python for Java developers book and implemented this in a few hours.

This is a simple REST based service application that I developed when I was learning about web services. The application loads a file containing production data (products.json) to in an in-memory map at startup and provides the following end-points for querying for product related data:


```
/search/category - returns a list of all known product categories 
/search/category/{category} - returns a list of all products for the provided category (example: /search/category/upright%20brooms)
/search/category/{category}/keyword/{word} - returns a list of products for the provided category and keyword (example: /search/category/upright%20brooms/keyword/clean)
/search/keyword - returns a list of all known product keywords (keywords are based on the title)
/search/keyword/{word} - returns a list of products for the provided keyword
```

## Requirements:
* Python (developed using version 3.9)
* Falcon
* Waitress

## Instructions:
* To start the server, run `python AppServer.py`
* The server will listen locally on port 8000
* Go to http://localhost:8000/search/category (or one of the other end-points)

## License
[MIT](https://choosealicense.com/licenses/mit/)
