"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# All the integers will be below 28123
# Create a function to determine if a number is abundant or not.
# Create a list that has abundant numbers appended to it when discovered
# If integer can be composed of two number from the list, then discard it. If cannot, add to the running total.
# It's good to be creating the list at the same time as testing the integers, as the two abundant numbers will always be lower than the integer.
# The above statement may not be true!!!

import time
start = time.time()

# function to determine abundancy
def abundant(num):
	sum = 0
	if num % 2 != 0:
		for n in range(1,int(num/2)+1,2): # iterate only though odd numbers to speed up
			if num % n == 0:
				sum += n
		if sum > num:
			return True
		else:
			return False
	else:
		for n in range(1,int(num/2)+1):
			if num % n == 0:
				sum += n
		if sum > num:
			return True
		else:
			return False

"""
ablist = [] # assign list of abundant numbers
total = 0 # assign total of integers which cannot be written as sum of two abundant numbers
for i in range(0,28124):
	is_sum = False # assign whether number is a sum of two abundants or not
	if abundant(i) == True:
		ablist.append(i) # if proven to be abundant, add to the list
	if i < 24:
		total += i # question states 24 is lowest sum of two abundants
	else: # for numbers more than 24
		for x in ablist: # iterate through abundant number list
				for y in ablist: # and again
					if x + y == i: # determine if i is a sum of two abundants
						is_sum = True
	if is_sum == False: # if not a sum of abundants, is_sum remains false and we can add the integer to our total
		total += i
print (total)
"""
# code takes ages to execute. How to shorten?
# maybe create code that does the opposite i.e. a list of numbers that ARE the sum of two abundants.
# iterate through all the numbers up to 28123 and sum them as long as they don't appear in the list.


ablist = [] # assign list of abundant numbers
total = 0 # assign total of integers which cannot be written as sum of two abundant numbers
for i in range(0,28124):
	is_sum = False
	for x in ablist:
		if i % x == 0: # check if i is a multiple of an abundant number, and therefore abundant itself
			ablist.append(i)
			break
	if i not in ablist: # now check if it's an abundant number
		if abundant(i):
			ablist.append(i) # add to the list if so
	for x in ablist: # iterate through abundant number list
		y = i - x # this is much quicker than old version of double iteration! (see comments below)
		if y in ablist:
			is_sum = True
			break
	if is_sum == False:
		total += i # if not sum of abundants
print (total)
# The above code gives the correct answer but still takes ages!

elapsed = (time.time() - start)
print (elapsed)

"""
		if is_sum == False: # only bother checking if it's not already been proven a sum
			for y in ablist: # and iterate again
				if x + y == i: # determine if i is a sum of two abundants
					is_sum = True
					break # as soon as determined that i is a sum, can leave for y loop
		else:
			break # break the for x loop once number is in the sumlist
"""