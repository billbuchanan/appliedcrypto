# Viewing crypto currency
# https://asecuritysite.com/encryption/doge
# Uses SoChain's API v3 (https://sochain.com/docs); no API key is needed.

from __future__ import print_function
import requests

API = 'https://sochain.com/api/v3'

def get_price(network):
	price = requests.get(API + '/price/' + network, timeout=10)
	info = requests.get(API + '/network_info/' + network, timeout=10)

	if price.status_code == 200 and info.status_code == 200:
		price = price.json()["data"]
		info = info.json()["data"]

		return price["value"],price["currency"],info["block_count"]
	return "","",""

val1=get_price("BTC")
val3=get_price("DOGE")
val4=get_price("LTC")
print("BTC:\t",val1[0],val1[1],"\tBlocks:\t",val1[2])
print("DOGE:\t",val3[0],val3[1],"\t\tBlocks:\t",val3[2])
print("LTC:\t",val4[0],val4[1],"\t\tBlocks:\t",val4[2])