"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.
Find the maximum total from top to bottom of the triangle below:
"""

triangle = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 "

#number of numbers in triangle:
n = 15+14+13+12+11+10+9+8+7+6+5+4+3+2+1 #or n* (n+1)/2
#use similar code from problem 18 to get numbers from string into one long array of integers
original_array = triangle.split() #default token is space

triangle_array = []
counter = 0
for i in range(1,16):
	holder_array = []
	for j in range(i):
		holder_array.append(int(original_array[counter]))
		counter += 1
	triangle_array.append(holder_array)
print (triangle_array)


for row in range(13,-1,-1):
	for i in range(row+1):
		if triangle_array[row+1][i] > triangle_array[row+1][i+1]:
			triangle_array[row][i] += triangle_array[row+1][i]
		else:
			triangle_array[row][i] += triangle_array[row+1][i+1]

print (triangle_array[0][0])





"""
below doesn't work as variables are global so keep getting changed in both. Use global variables for constants eg
speed of light!
global total, row, index, i
total = 0
row = 1
index = 0
i = 0

def route_total(current_total):
	global total, row, index, i
	if row > 15:
		print (current_total)

	if row <= 15:
		index += i
		current_total += triangle_array[index]
		i += 1
		route_total(current_total)
	
	if row <= 15:
		index += i
		current_total += triangle_array[index+i]
		i += 1
		route_total(current_total)

route_total(15)
		
# backwards calculation eliminates certain routes
"""
