#!/usr/bin/python
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1

print "Python Scripting L2 Hands-on_Assignment:08"
print " "

f = fibonacci(10)
for x in f:
    print x,