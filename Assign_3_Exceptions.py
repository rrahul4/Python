#!/usr/bin/python
print "Python Scripting L2 Hands-on_Assignment:03"
print " "
c = 0
def f2(x):
  try:
    print("Inside Try Block")
    c+= 1
    b = x + c
    print c
    return b
  except (UnboundLocalError):
    print("This is to Handle Exception UnboundLocalError")
  finally:
    print("Inside Finally Block")
print f2(1)
print c