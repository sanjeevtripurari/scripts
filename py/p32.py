import random
limit=7
answer=random.randint(1,100)
guesses=0
wins=False
while guesses<limit and not wins:
	guess=int(raw_input('Your guess is: '))
	print 'TRACE: ', guesses, limit,answer
	guesses+=1
	if guess == answer:
		print 'You win!'
		wins=True
	else:
		if guess > answer:
			print 'Too large'
		else:
			print 'Too small'
else:
	if not wins:
		print 'You lose.'
