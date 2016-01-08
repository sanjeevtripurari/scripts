def palindrome(n):
	l=list(str(n))
	r=l[::-1]
	return l==r
