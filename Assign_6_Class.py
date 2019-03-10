#!/usr/bin/python
import math
class ParentClass:
    def Fun_Sqroot(self, x):
        print "The Square Root of %d is %d" %(x,math.sqrt(x))
        return " "
    def Fun_Addition(self, x, y):
        print "The Addition of %d and %d is %d" %(x,y,x+y)
        return " "
    def Fun_Subtraction(self, x, y):
        print "The Subtraction of %d and %d is %d" %(x,y,x-y)
        return " "
    def Fun_Multiplication(self, x, y):
        print "The Multiplication of %d and %d is %d" %(x,y,x*y)
        return " "
    def Fun_Division(self, x, y):
        print "The Division of %d and %d is %d" %(x,y,x/y)
        return " "

class ChildClass(ParentClass):
	pass

print "Python Scripting L2 Hands-on_Assignment:06"
print " "
child=ChildClass()
print(child.Fun_Sqroot(100))
print(child.Fun_Addition(4,6))
print(child.Fun_Subtraction(10,7))
print(child.Fun_Multiplication(4,6))
print(child.Fun_Division(10,2))

