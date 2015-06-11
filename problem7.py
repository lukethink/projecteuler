"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

def is_prime(x):
	if x > 2:
		for i in range(2,x-1):
			if x % i == 0:
				return False
		return True
	elif x == 2:
		return True
	else:
		return False

i = 0 #iteration
x = 1 #number being tested
nth = 10001 #target nth prime number
while i < nth:
	if is_prime(x) == True:
		i += 1
		if i == nth:
			print (x)
	x += 1
	