#!/usr/bin/python

var = 100
i = 0
if(var == 100) : print ("why hello")


while(i < 10):
	print("gahhhh")
	i+=1
	
for letter in 'Hello':
	if(letter == 'H'):
		pass
		print("We are on ",letter)

	if(letter == 'e'): continue
	print('Current Letter :', letter)
	if(letter == 'l'): break
	
	
fam = ['andy','ro','lola']
for name in fam:
	print('Current person :', name)

print("Goodbye")