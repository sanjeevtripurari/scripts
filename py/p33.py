m=0		# the start
n=100		# the end
s=0		# the sum

i=m
while i<=n:
	s+=i
	i+=1

print 'The sum of integers from %d to %d is %d' % (m, n, s)
