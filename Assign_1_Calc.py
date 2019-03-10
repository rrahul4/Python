import math
def Calc_Factorial(x):
	print "This is Calc_Factorial Function"
	print "The Factorial of %d is %d" %(x,math.factorial(x))
	return " "
def Calc_Log10(x):
	print "This is Calc_Log10 Function"
	print "The Log10 of %d is %d" %(x,math.log10(x))
	return " "
def Calc_Radians(x):
	print "This is Calc_Radians Function"
	print "The Radians of %d is %d" %(x,math.radians(x))
	return " "
def Calc_Trig(x,y):
	print "This is Calc_Trig Function"
	if (y == "Sin" or y == "sin"):
		print "The Sine of %d is %f" %(x,math.sin(x))
	elif (y == "Cos" or y == "cos"):
		print "The Cosine of %d is %f" %(x,math.cos(x))
	elif (y == "Tan" or y == "tan"):
		print "The Tangent of %d is %f" %(x,math.tan(x))
	return " "