"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

#here's my function for finding the factorial of any number
def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n = n-1
	else:
		return result

#now to turn the result into a string and add the digits
def sum_of_digits(x):
	total = 0
	for i in str(x):
		total += int(i)
	return total

#here goes!
print (sum_of_digits(factorial(100)))


