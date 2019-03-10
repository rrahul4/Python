#!/usr/bin/python
import re
print "Python Scripting L2 Hands-on_Assignment:05"
print " "
StringList= ['Cooking is great hooby', 'India is great country','Reading a Book is great']
for SampleString in StringList:
	print(re.findall(r'\S*[aAeEiIoOuUyY]\S*[aAeEiIoOuUyY]\S*', SampleString))