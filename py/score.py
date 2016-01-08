score=float(raw_input('Enter a score: '))
if 85 <= score <= 100:
	print 'A'
elif 70 <= score < 85:
	print 'B'
elif 50 <= score < 70:	
	print "C"
elif 0 <= score < 50:
	print 'D'
else:
	print 'Invalid score entered'
