"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

#For starters, let's bring back the is_prime function from problem 7!
def is_prime(x):
	if x > 2:
		for i in range(2,int(x**0.5)+1):
			if x % i == 0:
				return False
		return True
	elif x == 2:
		return True
	else:
		return False

sum = 2 #initialise the sum variable - primes will be added to this for the total.
#start with 2, the only even prime number, as we will not be iterating through evens
i = 1 #i is the number that will be tested for prime status then added to sum if it is
while i < 2000000:
	if is_prime(i) == True:
		sum += i
	i += 2 #iterate only through odd numbers as evens cannot be primes
print (sum)