#!/usr/bin/python
import math
class FirstClass(object):
    def method1(self):
        print "This is From FirstClass"
class SecondClass(FirstClass):
    def method1(self):
        print "This is From SecondClass"
        super(SecondClass, self).method1()
class ThirdClass(FirstClass):
    def method1(self):
        print "This is From ThirdClass"
        super(ThirdClass, self).method1()
class FourthClass(SecondClass, ThirdClass):
    def method1(self):
        print "This is From FourthClass"
        super(FourthClass, self).method1()
        return " "

print "Python Scripting L2 Hands-on_Assignment:07"
print " "
print FourthClass.__mro__
obj=FourthClass()
print(obj.method1())

