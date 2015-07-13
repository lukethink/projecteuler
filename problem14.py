"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

#below gives the correct answer but takes 5mins+ computation time.
#Could be shortened by working out a particularly long chain and setting so that if a chain
#reaches that number, then a certain amount is added to chain_length

longest_chain = 1
for i in range(1,1000000):
	chain_length = 0
	n = i
	while n > 0:
		chain_length += 1
		if n == 1:
			if chain_length > longest_chain:
				longest_chain = chain_length
				result = i
			break
		elif n % 2 == 0:
			n = n/2
		else:
			n = (3*n) + 1
print (longest_chain)
print (result)