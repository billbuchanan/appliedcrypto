n=101*23
r=13

s1=5
s2=7
s3=3

a1=1
a2=0
a3=1

print 'N=',n
x = (r**2) % n
print 'x=',x
print 's1=',s1,'s2=',s2,'s3=',s3
print 'a1=',a1,'a2=',a2,'a3=',a3

y = (r * ((s1**a1) * (s2**a2) * (s3**a3)) ) % n
print 'Y=',y, ' y^2 mod n = ',(y**2 % n)

v1=(s1**2) %n
v2=(s2**2) %n
v3=(s3**2) %n

y2 = (x * ( (v1**a1) * (v2**a2) * (v3**a3)) ) % n
print 'Y=',(y**2) %n