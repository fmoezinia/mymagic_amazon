from amazon.api import AmazonAPI

def func(product):
	#insert amazon web services credentials
	AMAZON_ACCESS_KEY = 'AKIAJGEKFL3UEU6QMCPQ'
	AMAZON_SECRET_KEY = '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'
	#associate TAG must be updated every 180 days, make new amazon associates account to get new tag
	AMAZON_ASSOC_TAG = 'ignacio0ba-20'

	amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

	products = amazon.search_n(1,Keywords= product, SearchIndex= "All")

	print products
func('socks')