import random
s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
command=raw_input('Generate random letter? [Y/N] ')
while command == 'Y':
	i=random.randint(0,len(s)-1)
	print s[i]
	command=raw_input('Generate random letter? [Y/N] ')
print 'Bye'
