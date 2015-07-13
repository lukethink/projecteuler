"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

# lowest number is 0123456789; highest number is 9876543210.
# need way of working through these numbers but discounting duplications of numbers.
# in lexiography (?!), there's a pattern. So you work your way through the numbers starting with 0 first, then 1, then 2 etc.
# the possible permutations of starting with 0 can be calculated using a factorial function
# can work out the permutations for numbers starting with 0, then with 1, 2 etc. It will be the same for each one.
# this method should get us the first digit of the set of permutations which includes the millionth.
# from then on, can iterate through in some way to work out the millionth. Let's see!

# from problem 20, I wrote up the following function:
def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n = n-1
	else:
		return result

# number of permutations of 123456789 (remain starting with 0):
# print (factorial(9)) # 9 numbers
# 362880 combinations.
# This number * 3 is more just over 1,000,000, so we know that the millionth permutation begins with 2.
# It's now possible to move to the second number and work out the combinations starting with 0, i.e. 8!.

def nth_permutation(string, nth):
	i = 0 # iterator for the nth permutation
	j = 0 # iterator for the string # 
	result = "" # the number of the nth permutation as a list
	while i < nth:
		n = len(string) - 1
		i += factorial(n) # number of combinations with a fixed number in position at start
		j += 1 # change the fixed number to the next one along
		if i >= nth: # when i overshoots the desired nth permutation
			result += string[j-1] # we know this number has that position in the final answer
			i -= factorial(n) # go back down
			string = string.replace(string[j-1], "") # remove that number from the string
			j = 0
		if string == "":
			break
	print(result)

nth_permutation("0123456789", 1000000)
