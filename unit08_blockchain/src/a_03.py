# Viewing crypto currency
# https://asecuritysite.com/encryption/doge

import requests
import json 

def get_price(network):
	response = requests.get('https://chain.so/api/v2/get_info/'+network)
	
	if response.status_code == 200:
		content = response.json()

		return content["data"]["price"],content["data"]["price_base"],content["data"]["blocks"]
	return "",""

val1=get_price("BTC")
val2=get_price("DASH")
val3=get_price("DOGE")
val4=get_price("LTC")
print "BTC:\t",val1[0],val1[1],"\tBlocks:\t",val1[2]
print "DASH:\t",val2[0],val2[1],"\t\tBlocks:\t",val2[2]
print "DOGE:\t",val3[0],val3[1],"\t\tBlocks:\t",val3[2]
print "LTC:\t",val4[0],val4[1],"\t\tBlocks:\t",val4[2]