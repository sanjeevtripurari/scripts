class Student:
	stuCount=0
	def __init__(self,name, age):
		self.name=name
		self.age=age
		Student.stuCount+=1
	
	def displayCount(self):
		print "Total Number of Students %d" % Student.stuCount
	
	def displayStudent(self):
		print "Name: ",self.name, ", Age: ",self.age

stu1=Student("Rob",24)
stu1.displayCount()
stu1.displayStudent()

stu2=Student("Alice",25)
stu2.displayCount()
stu2.displayStudent()

