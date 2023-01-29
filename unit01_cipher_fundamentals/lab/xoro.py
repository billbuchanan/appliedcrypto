import sys

val1=54253124354024
val2=5395042653908

if (len(sys.argv)>1):
	val1=int(sys.argv[1])

if (len(sys.argv)>2):
	val2=int(sys.argv[2])

def bin2chr(data):
	result = ''
	
	while data:
		char = data & 0xff
		result += chr(char)
		data >>= 8
	
	return result


class Xoroshiro128Plus(object):
	def __init__(self, seed):
		self.seed = seed
	
	@staticmethod
	def rotl(x, k):
		return ((x << k) & 0xffffffffffffffff) | (x >> 64 - k)
	
	def next(self):
		s0 = self.seed[0]
		s1 = self.seed[1]

		result = (s0 + s1) & 0xffffffffffffffff
		
		s1 ^= s0

		self.seed[0] = self.rotl(s0, 55) ^ s1 ^ ((s1 << 14) & 0xffffffffffffffff)
		self.seed[1] = self.rotl(s1, 36)
		
		return result

print ("Seed 1:\t",val1)
print ("Seed 2:\t",val2)
print

generator = Xoroshiro128Plus([val1, val2]) 
for i in range(10):
	val=generator.next()
	print (i,hex(val),'\t',end='')
	print (repr(bin2chr(val)))

print ('\nCoin flip (60)')
generator = Xoroshiro128Plus([val1, val2]) 
count=0
for i in range(60):
	val=generator.next()
	bit = val & 0x1
	if (bit==0):
		count = count+1
		print ("H",end='')
	else:
		print ("T",end='')

print ()
print ('Heads:\t',count)
print ('Tails:\t',60-count)