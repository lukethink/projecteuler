"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

#Function to find nth triangle number
def triangle(x):
	number = (x*(x+1)) / 2
	return number

#Function for number of factors in a number x
def number_of_factors(y):
	result = 2
	for i in range(2,int((y-1)**0.5)):
		if y % i == 0:
			result += 2 #because of partner the other side of square root
	return result

#Finding first triangle number with over 500 factors
n = 1
while n > 0:
	if number_of_factors(triangle(n)) > 500:
		print (triangle(n))
		break
	else:
		n += 1