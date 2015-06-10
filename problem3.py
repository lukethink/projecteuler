# function to test if number is prime
def is_prime(x):
	if x > 2:
		for i in range(2, x-1):
			if x % i == 0:
				return False
		else:
			return True
	elif x == 2:
		return True
	else:
		return False

n = 600851475143

for x in range(1,n):
	if n % x == 0:
		if is_prime(x) == True:
			print (x)