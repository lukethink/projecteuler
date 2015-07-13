"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

# Create a function that creates Fibonnacci numbers
# Push numbers into a list
# Keep calling the function until len(result) == 1000

# function that produces all fibonnaci numbers up to nth number with a specified length:
def fibonnaci(length):
	numbers = [1,1] # a list to store the last two fibonnaci numbers
	n = 1 # n is the last number added to the sequence.
	i = 2 # we start iterating from the second number in the series.
	while len(str(n)) < length: # string because using length function.
		n = numbers[0] + numbers[1]
		numbers.append(n)
		del numbers[0] # so that the list takes up less memory
		i += 1 # i moves up one
	if len(str(n)) == length:
		print (i)
		print (numbers)

fibonnaci(1000)
			
		
	
	