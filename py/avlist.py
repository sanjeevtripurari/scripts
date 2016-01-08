#!/usr/bin/python

def sumlists(l):
	s=[]
	for subl in l:
		s.append(float(sum(subl))/len(subl))	# average
	return s

j=sumlists([[90, 95, 100, 100],[80,70,65,71],[95,60,75,55]])
print j
