def factorial(n):
	return reduce(lambda x,y:x*y, range(1,n+1))

j=factorial(5)
print j
