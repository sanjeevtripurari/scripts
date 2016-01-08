temperature=float(input('What is the temperature? '))
humidity=float(input('What is the humidity? '))
if temperature > 65:
	print ('Wear shorts.')
	if humidity >= 80:
		print ('Go Shirtless')
else:
	print ('Wear Jeans')
print('Enjoy the Sun.')
