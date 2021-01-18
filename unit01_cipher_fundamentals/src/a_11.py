# Bit shift
# https://asecuritysite.com/comms/shift
import sys

val1="00110101"

if (len(sys.argv)>1):
        val1=sys.argv[1]

print ("Binary form:  \t\t",val1)
dec=int(val1,2)

print ("Decimal form:  \t\t",dec,"\t",bin(dec)[2:10].rjust(8,'0'))

res=(dec << 1) & 0xff
print ("Shift left  (1):\t",res,"\t",bin(res)[2:10].rjust(8,'0'))

res=(dec << 2) & 0xff

print ("Shift left  (2):\t",res,"\t",bin(res)[2:].rjust(8,'0'))

res=(dec >> 1) & 0xff
print ("Shift right (1):\t",res,"\t",bin(res)[2:10].rjust(8,'0'))

res=(dec >> 2) & 0xff
print ("Shift right (2):\t",res,"\t",bin(res)[2:10].rjust(8,'0'))
