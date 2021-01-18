![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

A.6
```python
print 0x43 | 0x21
print 0x43 & 0x21
print 0x43 ^ 0x21
```

A.7
```python
val1=93
print "Dec:\t",val1
print "Bin:\t",bin(val1)
print "Hex:\t",hex(val1)
print "Oct:\t",oct(val1)
print "Char:\t",chr(val1)
```
A.8
```python
val=93
console.log(val.toString(2))
console.log(val.toString(16))
console.log(val.toString(8))
console.log(String.fromCharCode(val))
```
A.9
```python
import base64
str="crypto"
print base64.b64encode(val)
```
A.10
```python
import sys

val1="00110101"

if (len(sys.argv)>1):
        val1=sys.argv[1]

print "Binary form:  \t\t",val1
dec=int(val1,2)

print "Decimal form:  \t\t",dec,"\t",bin(dec)[2:10].rjust(8,'0')

res=(dec << 1) & 0xff
print "Shift left  (1):\t",res,"\t",bin(res)[2:10].rjust(8,'0')

res=(dec << 2) & 0xff

print "Shift left  (2):\t",res,"\t",bin(res)[2:].rjust(8,'0')

res=(dec >> 1) & 0xff
print "Shift right (1):\t",res,"\t",bin(res)[2:10].rjust(8,'0')

res=(dec >> 2) & 0xff
print "Shift right (2):\t",res,"\t",bin(res)[2:10].rjust(8,'0')
```
B.1
```python
def gcd(a, b):
    
	while( b != 0 ):
		Remainder = a % b;
		a = b;
		b = Remainder;
	return a;

g = gcd(54,8)
print g
```
C.3

```python
message = raw_input('Enter message: ')
e =  raw_input('Enter exponent: ') 
p = raw_input('Enter prime ')

cipher = (int(message) ** int(e)) % int(p)
print cipher
```
D.1
```python
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
```
D.2
```python
import sys

test=1000

if (len(sys.argv)>1):
	test=int(sys.argv[1])

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
 
print sieve_for_primes_to(test)
```
