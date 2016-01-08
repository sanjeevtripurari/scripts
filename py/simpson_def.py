def simpson(f, a, b, n):
	d=float(b-a)/n

	# f(a)
	fa=f(a)

	# f(b)
	fb=f(b)
	
	#sum f(a+id)
	s1=0
	i=1

	while i<=n-1:
		s1 += f(a+i*d)
		i+=1
	#sum f(a+(i+0.5)d)
	s2=0
	i=0

	while i<=n-1:
		s2 +=  f(a+(i+0.5)*d)
		i += 1
	# area
	s= (d/6) * (fa+2*s1+4*s2+fb)
	return s

#print "The intgral is equal to ", simpson(lambda x: x*x, 0, 10, 10000)
	
