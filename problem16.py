"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

def sum_digits(n):
	sum = 0
	n = str(n)
	for i in n:
		sum += int(i)
	print (sum)

sum_digits(2**1000)

#really easy!!!