import passlib.hash;
string="hello"
print ("LM Hash:"+passlib.hash.lmhash.encrypt(string))
print ("NT Hash:"+passlib.hash.nthash.encrypt(string))

