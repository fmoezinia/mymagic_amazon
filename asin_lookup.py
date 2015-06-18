import re
from amazon.api import AmazonAPI

AMAZON_ACCESS_KEY = 'AKI...JP2'
AMAZON_SECRET_KEY = 'Eto...uxV'
AMAZON_ASSOC_TAG = 'p...1'

asin_regex = r'/([A-Z0-9]{10})'
isbn_regex = r'/([0-9]{10})'

def get_amazon_item_id(url):
    # return either ASIN or ISBN
    asin_search = re.search(asin_regex, url)
    isbn_search = re.search(isbn_regex, url)
    if asin_search:
        return asin_search.group(1)
    elif isbn_search:
        return isbn_search.group(1)
    else:
        # log this URL
        return None

def get_amazon_product_meta(url):
    # the input URL is always of amazon
    amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region="IN")

    item_id = get_amazon_item_id(url)
    if not item_id:
        return None

    try:
        product = amazon.lookup(ItemId=item_id)        
    except amazon.api.AsinNotFound:
        # log this ASIN
        return None

    # product.price_and_currency returns in the form (price, currency)
    product_price = product.price_and_currency[0]