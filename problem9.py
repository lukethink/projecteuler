"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

"""My observations:
a < b
b < c
a**2 + b**2 = c**2
a + b + c = 1000
product = a*b*c

c can be expressed in terms of a and b with two simultaneous equations:
c = 1000 - a - b
c = (a**2 + b**2)**0.5

So, a + b + c = 1000 can also be expressed as:
a + b + (a**2 + b**2)**0.5 = 1000

If a + b + c = 1000 and a<b<c:
the min value of a is 1 and max value is 332
the min value of b is 2 and max value is 499
the  minimum possible value of c is 334 and max value is 997
"""

for a in range(1,333):
	for b in range(2,500):
		c = 1000 - a - b
		product = a*b*c
		if a + b + (a**2 + b**2)**0.5 == 1000:
			print (a)
			print (b)
			print (c)
			print (product)
