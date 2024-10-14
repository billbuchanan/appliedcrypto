import passlib.hash;

def hashes(to_hash):
    print ("LM Hash:"+passlib.hash.lmhash.hash(to_hash))
    print ("NT Hash:"+passlib.hash.nthash.hash(to_hash))

hashes("Napier")
hashes("Foxtrot")
