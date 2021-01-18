def gcd(a, b):
    
	while( b != 0 ):
		Remainder = a % b;
		a = b;
		b = Remainder;
	return a;

g = gcd(54,8)
print (g)
