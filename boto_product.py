import bottlenose

#region_options = bottlenose.api.SERVICE_DOMAINS.keys(). region options can be added later


AWS_ACCESS_KEY_ID = 'AKIAJGEKFL3UEU6QMCPQ'
AWS_SECRET_ACCESS_KEY = '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'
#associate TAG must be updated every 180 days, make new amazon associates account to get new tag
AWS_ASSOCIATE_TAG = 'ignacio0ba-20'

amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)

#def product_lookup(item, category)


response = amazon.ItemSearch(Keywords="sock", SearchIndex="All")
print response