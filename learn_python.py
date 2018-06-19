#!/usr/bin/python

"""
python

"""

'''
first_name = input("Enter a ur first name: ")
last_name = input("Enter your last name: ")
initial = input("Enter your initial: ")

person = initial + " " + first_name + " " + last_name


print("Ur name is %s" %person)

print("Ur name is %s%s%s" %initial  %first_name  %last_name)
'''

catNames = []

while True:

	print('Enter the name of cat ' + str(len(catNames) + 1) +
		'(or enter Nothing to stop.):')

	name = input()

	if name == '':

		break

	catNames = catNames + [name] ##Append indirectly using list concatenation

print('The cat names are:')

for name in catNames:

	print(' ' + name)
