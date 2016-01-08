#!/usr/bin/env python

a=1
def f(x):
	def g(x):
		return x*(y+1)
	y=1
	z=g(x+1)+y
	return z

b=f(1)
print b
