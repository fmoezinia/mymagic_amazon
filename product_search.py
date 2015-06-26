from amazon.api import AmazonAPI

#WILL NOT WORK WITH OUT OS.ENVIRON CREDENTIALS FROM AWS AMAZON ETC


class Itemsearch(object):
	

	def __init__(self, product):
		self.product = product

	def prod_search(self):

		#insert amazon web services credentials
		#associate TAG must be updated every 180 days, make new amazon associates account to get new tag

		amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

		products_found = amazon.search_n(1,Keywords= self.product, SearchIndex= "All")

		try: 
			return products_found[0].title
		except IndexError:
			return 'No such item available'

	def prod_asin(self):

		#insert amazon web services credentials
		AMAZON_ACCESS_KEY = 'AKIAJGEKFL3UEU6QMCPQ'
		AMAZON_SECRET_KEY = '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'
		#associate TAG must be updated every 180 days, make new amazon associates account to get new tag
		AMAZON_ASSOC_TAG = 'ignacio0ba-20'

		amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

		products_found = amazon.search_n(1,Keywords= self.product, SearchIndex= "All")

		
		try: 
			return products_found[0].asin
		except IndexError:
			return 'No product available'	

	

	def prod_price(self, product_asin):
		#insert amazon web services credentials
		AMAZON_ACCESS_KEY = 'AKIAJGEKFL3UEU6QMCPQ'
		AMAZON_SECRET_KEY = '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'
		#associate TAG must be updated every 180 days, make new amazon associates account to get new tag
		AMAZON_ASSOC_TAG = 'ignacio0ba-20'

		amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

		the_product = amazon.lookup(ItemId='' + product_asin + '')

		found_product_price = the_product.price_and_currency



# customer_product = Itemsearch(product)
customer_product = Itemsearch('arsenal shirt')

product_name = customer_product.prod_search()
print product_name
product_asin = customer_product.prod_asin()
print product_asin
product_price_and_currency = customer_product.prod_price(product_asin)
print product_price_and_currency







#class Item_asin_search(Itemsearch):


#adding item to cart


	


