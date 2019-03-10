#!/usr/bin/python
import time
def my_decorator(func):
    def wrapper():
        print "Time Start " 
        start = time.time()
        func()
        end = time.time()
        print "Time End" 
        print "Elapsed time: ", str(end - start), "Start : ", start, "End : ", end
    return wrapper

def my_method():
    print("This is actual Method !")

my_method = my_decorator(my_method)

print "Python Scripting L2 Hands-on_Assignment:10"
print " "
my_method()