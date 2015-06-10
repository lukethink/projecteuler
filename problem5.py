# Smallest number divisble by all numbers from 1 to 20

smallest_number = 1
while smallest_number > 0:
	for x in range(1,21):
		if smallest_number % x != 0:
			smallest_number += 1
		else:
			break
			print (smallest_number)
