# Q4 Find largest palindrome made from product of two three-digit numbers
# Largest possible number made from product of two three-digit numbers is 998001 (999 * 999)
# Smallest possible number made from product of two three-digit numbers is 10000 (100 * 100)

palindromes = []
for x in range(100,1000):
	for y in range(100,1000):
		z = x * y #z is all numbers that are a product of two three-digit numbers
		z = str(z)
		if z == z[::-1]: #i.e. if it's a palindrome
			palindromes.append(int(z))

print(sorted(palindromes))

"""
for n in range(10000,998001):
	n = str(n)
	if n == n[::-1]: #i.e. if it's a palindrome
		for i in range(100,1000): #for all 3-digit values of i
			if len(str(int(n)/i)) == 3: #check if dividing palindrome by 3-digit number equals another 3-digit number
				print (int(n)) #if so, print that palindrome
"""