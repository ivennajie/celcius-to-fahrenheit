#!/usr/bin/env python

while True:
	try:
		celsius = int(input("Enter degree in Celsius: "))
	except ValueError:
		print("Please enter a valid number!")
		continue
	else:
		break
	
def conv(c):

	return (9/5*c+32)

fahrenheit = conv(celsius)
print(fahrenheit)

