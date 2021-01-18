# Ethereum details
# https://asecuritysite.com/encryption/eth

import json

apikey='***YOUR API KEY HERE****'


def geneth(module,action,addr="",tag="",addition="",txhash=""):


	if (addr<>""): addr="&address="+addr
	if (tag<>""): tag="&tag="+str(tag)
	if (txhash<>""): txhash="&txhash="+str(txhash)
	st='http://api.etherscan.io/api?module='+module+'&action='+action+'&apikey='+apikey+addr+tag+txhash+addition
	content,res= httplib2.Http().request(st)
	d=json.loads(res) 
	return d



v = geneth('stats','ethsupply')
print "Eth supply:\t\t\t",v['result']

v = geneth('stats','ethprice',"")
print "Eth price ($):\t\t\t",v['result']['ethusd']


v = geneth('proxy','eth_gasPrice')
gas=int(v['result'],16)
print "Gas price:\t\t\t",gas," Wei (", gas/1e18,"Eth)"


v = geneth('proxy','eth_blockNumber')
block=v['result']
print "Most recent block:\t\t",int(v['result'],16)


v = geneth('proxy','eth_getBlockTransactionCountByNumber',tag=block)
count=v['result']
print " No of trans in block:\t\t",int(count,16)


v = geneth('proxy','eth_getBlockTransactionCountByNumber',tag="0x10FB78")
res=v['result']
print "No of trans in Block 0x10FB78:\t",res

v = geneth('proxy','eth_getTransactionByHash',txhash="0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1")
res=v['result']
print "Transaction by 0x1e..c1:\t",json.dumps(res,indent=4, sort_keys=True)



v = geneth('proxy','eth_getCode',addr="0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c", tag='latest')
res=v['result']
print "Ethcode for 0xf75..d0c:\t",res


v = geneth('account','balance',addr="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a")
block=v['result']
print "Account balance for 0xdd..121a:\t",v['result']," Wei (", int(block)/1e18,"Eth)"

v = geneth('account','getminedblocks',addr="0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b")
res=v['result'][0]
print "First mined blocks by  0x9dd..46:\t",json.dumps(res,indent=4, sort_keys=True)
import httplib2
import json

apikey='***YOUR API KEY HERE****'


def geneth(module,action,addr="",tag="",addition="",txhash=""):


	if (addr<>""): addr="&address="+addr
	if (tag<>""): tag="&tag="+str(tag)
	if (txhash<>""): txhash="&txhash="+str(txhash)
	st='http://api.etherscan.io/api?module='+module+'&action='+action+'&apikey='+apikey+addr+tag+txhash+addition
	content,res= httplib2.Http().request(st)
	d=json.loads(res) 
	return d



v = geneth('stats','ethsupply')
print "Eth supply:\t\t\t",v['result']

v = geneth('stats','ethprice',"")
print "Eth price ($):\t\t\t",v['result']['ethusd']


v = geneth('proxy','eth_gasPrice')
gas=int(v['result'],16)
print "Gas price:\t\t\t",gas," Wei (", gas/1e18,"Eth)"


v = geneth('proxy','eth_blockNumber')
block=v['result']
print "Most recent block:\t\t",int(v['result'],16)


v = geneth('proxy','eth_getBlockTransactionCountByNumber',tag=block)
count=v['result']
print " No of trans in block:\t\t",int(count,16)


v = geneth('proxy','eth_getBlockTransactionCountByNumber',tag="0x10FB78")
res=v['result']
print "No of trans in Block 0x10FB78:\t",res

v = geneth('proxy','eth_getTransactionByHash',txhash="0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1")
res=v['result']
print "Transaction by 0x1e..c1:\t",json.dumps(res,indent=4, sort_keys=True)



v = geneth('proxy','eth_getCode',addr="0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c", tag='latest')
res=v['result']
print "Ethcode for 0xf75..d0c:\t",res


v = geneth('account','balance',addr="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a")
block=v['result']
print "Account balance for 0xdd..121a:\t",v['result']," Wei (", int(block)/1e18,"Eth)"

v = geneth('account','getminedblocks',addr="0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b")
res=v['result'][0]
print "First mined blocks by  0x9dd..46:\t",json.dumps(res,indent=4, sort_keys=True)