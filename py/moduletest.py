# Define variables
numberone=1
ageofgradma=79

#define some functions
def printhello():
	print "hello"

def timesfour(input):
	print input * 4

#define a class
class baseballCard:
	def __init__(self):
		self.brand=raw_input("What brand is the card? ");
		self.player=raw_input("What player is on the card? ");
		self.price=raw_input("How much did it cost? ")
		self.age=raw_input('How old is it (in years)?')

	def printdetails(self):
		print "This card is of "+self.player 
		print self.brand," card, of "+self.player," is "+self.age
		print " years old and costs " + self.price+" dollars."

