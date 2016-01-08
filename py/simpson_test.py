import simpson_def
import math

print "The integral of x^3 between 0 and 10 is", simpson_def.simpson(lambda x:x*x*x, 0, 10, 10000)
print "The integral of sin(x) between 0 and 1 is", simpson_def.simpson(math.sin, 0, 1, 10000)
print "The integral of log(x) between 0 and 1.5 is", simpson_def.simpson(math.log, 1, 1.5, 10000)

