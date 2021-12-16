#!/usr/bin/env python

import sys

celsius = input("Enter degree in Celsius: ")
try:
	celsius = int(celsius)
except ValueError:
	print("Please enter a valid number!")
	sys.exit(0)

def conv(c):

	return (9/5*c+32)

fahrenheit = conv(celsius)
print(fahrenheit)

