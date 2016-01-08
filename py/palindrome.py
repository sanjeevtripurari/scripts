def palindrome(n):
	l=list(str(n))
	r=l[:]
	r.reverse()
	return l==r
