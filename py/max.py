import math
m=0
n=100
s=float('-inf')
i=m

while i<=n:
	f=math.sin(i*i)
	s=max(f,s)
	i+=1

print 'The maximum value of the function is',s
