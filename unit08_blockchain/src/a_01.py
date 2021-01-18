# https://asecuritysite.com/encryption/bit
# Bitcoin details

import httplib2

resp, content = httplib2.Http().request("https://blockchain.info/q/latesthash")
print "Latest hash: ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/bcperblock")
print "Block reward per block: ",int(content)/100000000.0

resp, content = httplib2.Http().request("https://blockchain.info/q/getblockcount")
print "Longest block: ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/getdifficulty")
print "Difficulty: ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/probability")
print "Mining probability: ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/interval")
print "Average time between blocks (seconds): ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/eta")
print "Time to next block (seconds): ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/marketcap")
print "Market capitalisation (Million USD): ",float(content)/1000000


resp, content = httplib2.Http().request("https://blockchain.info/q/24hrprice")
print "24hr price (USD): ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/24hrtransactioncount")
print "24hr transactions: ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/hashrate")
print "Hash rate: ",content

resp, content = httplib2.Http().request("https://blockchain.info/q/addressbalance/1GbVUSW5WJmRCpaCJ4hanUny77oDaWW4to?confirmations=1")
print "Account balance for 1Gb...4to (BTC): ",int(content)/100000000

resp, content = httplib2.Http().request("https://blockchain.info/q/getreceivedbyaddress/1GbVUSW5WJmRCpaCJ4hanUny77oDaWW4to?confirmations=1")
print "Received for 1Gb...4to (BTC): ",int(content)/100000000