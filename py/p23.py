def low_calorie(lowprice,):
	print "Chef: salad with low-fat dressing"
	return lowprice

def high_calorie(highprice,):
	print "Cheeseburger with French Fries"
	return highprice

lowprice=4.99
highprice=6.99

meal=float(input('Enter 1 for low calorie or 2 for high calorie meail? '))
if (meal==1):
	print low_calorie(lowprice)
else:
	print high_calorie(highprice)
