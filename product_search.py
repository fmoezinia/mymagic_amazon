from amazon.api import AmazonAPI




class Itemsearch(object):
	

	def __init__(self, product):
		self.product = product

	def prod_search(self):

		#insert amazon web services credentials
		AMAZON_ACCESS_KEY = 'AKIAJGEKFL3UEU6QMCPQ'
		AMAZON_SECRET_KEY = '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'
		#associate TAG must be updated every 180 days, make new amazon associates account to get new tag
		AMAZON_ASSOC_TAG = 'ignacio0ba-20'

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



customer_product = Itemsearch('xxxasdfasdfafdsx')
print customer_product.prod_search()
print customer_product.prod_asin()


#customer_product = Itemsearch(product)


#class Item_asin_search(Itemsearch):
	


