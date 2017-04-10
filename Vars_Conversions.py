#!/usr/bin/python

counter = 200          # An integer assignment
miles   = 12.4         # A floating point
name    = "Tom"        # A string

print counter
print miles
print name

#multi assignment
a = b = c =2
print(a + " " + b + " " + c)

d,e,f = 1,5.0,"Dar"
print(d + " " + e + " " + f)

#Deleting var
del d,e,f

#String - substring
str = 'Why hello there'

print str	 #prints full string
print str[0] #prints 1st char
print [2:5]	 #prints chars 3 - 5

#list
list = ['abd',2,333.0,'Tom',4/2]
print list	   #prints list
print list * 2 #prints list twice

#tuples - read only - can't increase size
tuple = ('avd',234,'wer')

print tuple