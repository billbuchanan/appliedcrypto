message = input('Enter message: ')
e =  input('Enter exponent: ') 
p = input('Enter prime ')

cipher = (int(message) ** int(e)) % int(p)
print (cipher)


