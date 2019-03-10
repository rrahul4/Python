#!/usr/bin/python
print "Python Scripting L2 Hands-on_Assignment:02"
print " "
try:
  print("Inside Try Block")
  a=input("Enter the value for a: \n")
  b=input("Enter the value for b: \n")
  result = a / b
  print(x)
except (KeyboardInterrupt):
  print("This is to Handle Exception KeyboardInterrupt")
except NameError:
  print("This is to Handle Exception NameError")
except ArithmeticError:
  print("This is to Handle Exception ArithmeticError")  
except:
  print("This is to Handle other Exceptions")
else:
	print("The division Result is : ", result)
finally:
	print("Inside Finally Block")