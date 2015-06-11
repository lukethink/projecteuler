# Smallest number divisible by all numbers from 1 to 10 is 2520
# Find smallest number divisible by all numbers from 1 to 20

"""Doesn't need to be divisible by all numbers from 1 to 20, simply because many are duplicate eg if divisible by 18, then also divisible by 3.
So, unique divisibles are:
20
19
18
17
16
15
14
13
12
11

Also, smallest number has to be an even number, as no odd number is divisible by an even number

Do not have to iterate through every number. Can progress through highest divisible, so +20 each time.
"""

smallest_number = 20 #assign smallest to begin
x = 11 #assign divisible to begin
while x < 21:
	if smallest_number % x == 0:
		x += 1
		if x == 20:
			print (smallest_number)
			break
	else:
		smallest_number += 20 #progress by 20 each time as it must be divisible by 20
		x = 11 #reset x to 11
			


"""Below code makes sense to me but ends up calculating forever! So need way to shorten
smallest_number = 2520
x = 2
while smallest_number > 1:
	while x > 1:
		if smallest_number % x != 0:
			smallest_number = smallest_number + 2
			x = 2
		else:
			x = x + 1
			if x == 21:
				break
				print (smallest_number)
"""
