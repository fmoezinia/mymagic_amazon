from amazon.api import AmazonAPI

class search(object):
		AMAZON_ACCESS_KEY = 'AKIAJGEKFL3UEU6QMCPQ'
		AMAZON_SECRET_KEY = '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'
		#associate TAG must be updated every 180 days, make new amazon associates account to get new tag
		AMAZON_ASSOC_TAG = 'ignacio0ba-20'

		

		def __init__(self, product):
			self.product = product

		def prod_search(self):

			amazon = AmazonAPI(AMAZON_ACCESS_KEY.search, AMAZON_SECRET_KEY.search, AMAZON_ASSOC_TAG.search)
			products_found = amazon.search_n(1,Keywords= self.product, SearchIndex= "All")
			return products_found[0].title

customer_product = search('arsenal shirt')
print customer_product.prod_search()