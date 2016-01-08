#!/usr/bin/env python

numbers=2,4,6,8,10

num_sum=0
count=0

for a in numbers:
	count=count+2
	print count
	if count==8:
		break
print count
