def printinfo(arg1, *vartuple):
	"This prints a variable passed arguements"
	print "This is the output"
	print arg1
	for var in vartuple:
		print var
	return

printinfo(100);
printinfo(20,30,40);
