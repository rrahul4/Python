#!/usr/bin/python
import re
print "Python Scripting L2 Hands-on_Assignment:04"
print " "
print(" This is Filter Digit at beginning and at ending of String")	
StringList1= ['1 Cooking is great hooby 9', '2 India is great country 8','3 Reading a Book is great 7']
for SampleString1 in StringList1:
  print(re.findall(r'^[1-9]', SampleString1))
  print(re.findall(r'[1-9]$', SampleString1))

print(" This is Find White Space or Word Characters")	
StringList2= ['1 Cooking is great hooby 9', '  ','3 Reading a Book is great 7']
for SampleString2 in StringList2:
	print(bool(re.match('^\s+$', SampleString2)))

print(" This is Find String containing no White Space characters ")	
StringList3= ['1 Cooking is great hooby 9', 'Wipro','3 Reading a Book is great 7']
for SampleString3 in StringList3:
	if( ' ' in SampleString3):
		print SampleString3 + " >> This String Contains White Spaces"
	else:
		print SampleString3 + " >> This String Contains No White Spaces"
