""" The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(x):
	result = 0
	for i in range(1,x+1):
		result += i**2
	return result

print (sum_of_squares(100))

def square_of_sum(x):
	result = 0
	for i in range(1,x+1):
		result += i
	result = result**2
	return result

print (square_of_sum(100))

print (square_of_sum(100) - sum_of_squares(100))