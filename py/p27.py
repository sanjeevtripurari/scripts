class Student:
	stuCount=0
	def __init__(self, name, age):
		self.name=name
		self.age=age
		Student.stuCount+=1

def displayCount(self):
	print "Total Number of Students %d " % Student.stuCount

def displayStudent(self):
	print "Name: ",self.name,", Age: ",self.age

print "Student.__doc__:     ",Student.__doc__
print "Student.__name__:    ", Student.__name__
print "Student.__module__:  ", Student.__module__
print "Student.__bases__:   ",Student.__bases__
print "Student.__dict__:     ",Student.__dict__
