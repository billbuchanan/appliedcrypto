import math

def get_if_prime(val):

	max = math.sqrt(val);

	if (val % 2 == 0):
		return (False); 
            
	if (val % 3 == 0):
		return (False); 

	for k in range(0, 10000):
		testval = 6 * k + 1;
                if (testval>max):
			break
                if (val % testval == 0):
			return (False)
                testval = 6 * k - 1;
                if (testval>max):
			break
 
                if (val % testval == 0):
			return (False)
	return (true)

val=93

res = get_if_prime(val)
if (res==True):
	print str(val)+" is prime"
else:	
	print str(val)+" is not prime"
