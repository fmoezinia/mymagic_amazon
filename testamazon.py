from amazon.api import AmazonAPI

api = API(locale='us')
items = api.item_search('Books', Publisher="O'Reilly")