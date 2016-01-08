class Student(object):
	def __init__(self):
		super(Student,self).__init__()

class Graduate(Student):
	def __init__(self):
		super(Graduate, self).__init__()

class Masters(Graduate):
	def __init__(self):
		super(Masters,self).__init__()

class GM(Graduate,Masters):
	def __init__(self):
		super(GM,self).__init__()
	
class Student(object):
	def __init__(self):
		pass

def message(self):
	print "I have finally graduated!"	

def Graduate(Student):
	def __init__(self):
		super(Graduate,self).__init__()

def message(self):
	print "I will now do my masters!"
	super(Graduate,self).message()


