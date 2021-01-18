import OpenSSL 

str="fred.pfx"
passwords=["ankle","battery","password","bill","apple","apples","orange"]

for password in passwords:
	try:
		pfx = open(str, 'rb').read()
		
		p12 = OpenSSL.crypto.load_pkcs12(pfx, password)

		print "Found: ",password
		print " ",p12.get_friendlyname()

		privkey=OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey())

		certificate=OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate())
		print privkey
		print certificate

	except:
		print "Not working: ",password
