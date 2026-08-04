country_code = {'India':'0091',
                'Australia':'0025',
                'Nepal':'00977'}

#search dictionary for country code of india
cc = input("Enter any country to get its country code:")
print("Country code of",cc,"is:",country_code.get(cc,'Not found!!'))