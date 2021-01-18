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
str=”crypto”
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
This works because we start with all the odd numbers up to the square root of the limit of the numbers we are looking for. If we have 100, then the size will be 50. We start off with odd numbers (as 2 is the only even prime):

<pre>
3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 .. 99
</pre>
In the first time round we have i equal to 1, and we will jump 3 each time and mark them as not prime:
<pre>
<b>3</b> 5 7 <s>9</s> 11 13 <s>15</s> 17 19 <s>21</s> 23 25 <s>27</s> 29 31 <s>33</s> 35 .. 97 <s>99</s>
</pre>
In the next time round, we will jump 5, starting at 5:
<pre>
3 <b>5</b> 7 X 11 13 <s>X</s> 17 19 X 23 <s>25</s> X 29 31 X <s>35</s> .. 97, X
</pre>
In the next time round, we will jump 7, starting at 7:
<pre>
3 5 <b>7</b> X 11 13 X 17 19 <s>X</s> 23 X X 29 31 X <s>X</s> .. 97 99
</pre>
In the next time round, we will jump 9, starting at 9:
<pre>
3 5 7 <b>X</b> 11 13 X 17 19 X 23 X <s>X</s> 29 31 X X .. 97 99
</pre>
In the end we stop at 19, and with a jump of 19, and add the value of 2 to the discovered prime numbers:
<pre>
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
</pre>
The marking of the factors follows this sequence:
<pre>
[1, 3, 5, 7, 9, 11,13,15,17,19,21,23,25,27,29,31,33,35 .. ]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, <b>1</b>, 1, 1, <b>0</b>, 1, 1, <b>0</b>, 1, 1, <b>0</b>, 1, 1, <b>0</b>, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
[1, 1, <b >1</b>, 1, 0, 1, 1, <b>0</b>, 1, 1, 0, 1, <b>0</b>, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
</pre>


