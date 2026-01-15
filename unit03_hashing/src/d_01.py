import passlib.hash;
string="hello"
print ("LM Hash:"+passlib.hash.lmhash.hash(string))
print ("NT Hash:"+passlib.hash.nthash.hash(string))

