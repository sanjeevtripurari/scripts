import random
limit=7
answer=random.randint(1,100)
guesses=0
wins=False
while guesses<limit :
	guess=int(raw_input('Your guess is: '))
	guesses+=1
	if guess == answer:
		print 'You win!'
		break
	else:
		if guess > answer:
			print 'Too large'
		else:
			assert guess < answer
			print 'Too small'
else:
	print 'You lose.'
