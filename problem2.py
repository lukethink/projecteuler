fib = [1,2]

i = 2
while i > 1:
	x = fib[i-1] + fib[i-2]
	fib.append(x)
	i += 1
	if x > 4000000:
		break

def sum_evens(numbers):
	result = 0
	for n in numbers:
		if n % 2 == 0 and n <= 4000000:
			result += n
	print (result)
		
sum_evens(fib)
	
