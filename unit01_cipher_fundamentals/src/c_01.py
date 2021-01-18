message = raw_input('Enter message: ')
e =  raw_input('Enter exponent: ') 
p = raw_input('Enter prime ')

cipher = (int(message) ** int(e)) % int(p)
print (cipher)
