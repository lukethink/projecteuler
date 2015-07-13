"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

"""
My observations:

At each point before moving forward, there is a binary choice to be made: right or down ('a' or 'b'?)

Regardless of route taken, the number of steps is the same. In a 2x2 grid, there are 4 moves.
In a 20x20 grid, there are 40 moves.

The number of right moves always equals the number of down moves over the course of the route.
So once ten right moves have been taken, the remainder of moves must be down.

There are 20 'a's and 20 'b's - we are asking, in how many unique ways can they be ordered?

We are looking for unique permutations i.e. the order does matter

Is answer just 2**40? (2 options to power of number of choices)
No because there must be 20 of each

To get half way through the grid (20 steps), number of routes are simply 2**20

NOT like balls in the bag because probability of right or down is equal until reaching the edge of the grid,
when it switches to 100% one way or another

Can calculate number of ways of reaching the right side, then double it to get total number of routes
"""

global total_routes
total_routes = 0

"""
def number_of_routes(x,y,limit): #where x and y are size of grid
	global total_routes
	if x == limit and y == limit:
			total_routes += 1
			print (total_routes)
	
	if x != limit:
		number_of_routes(x+1, y, limit)
	
	if y != limit:
		number_of_routes(x, y+1, limit)

#2 is 6
#3 is 20
#4 is 70
#5 is 252
#6 is 924
#7 is 3432
#8 is 12870
"""

#need central binomial coefficient from Pascal's triangle!
#formula for central coefficient 2n! / n!**2

import math

def number_of_routes(x):
	result = math.factorial(2*x) / math.factorial(x)**2
	print (result)

number_of_routes(20)
