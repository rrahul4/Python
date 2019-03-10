#!/usr/bin/python
class MyList(object):
    def __init__(self, lst):
        self.lst = lst
    def __reversed__(self):
        return MyReversedIterator(self.lst)

class MyReversedIterator(object):
    def __init__(self, lst):
        self.lst = lst
        self.pos = len(lst) - 1

    def __iter__(self):
        return self

    def next(self):
        if self.pos < 0:
            raise StopIteration()
        elem = self.lst[self.pos]
        self.pos -= 1
        return elem


print "Python Scripting L2 Hands-on_Assignment:09"
print " "

for i in reversed(MyList([1, 2, 3, 4])):
    print i