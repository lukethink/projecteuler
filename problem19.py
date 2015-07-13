"""
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

#create a year list of lengths of months, leaving out December due to firsts of months list later:
month_days = [31,28,31,30,31,30,31,31,30,31,30]
#second entry (28) will change to 29 during a leap year
	
#function to produce list of 1st days of month as 'x' day of the year, based on month_days:
def firsts_of_month(month_days):
	array = [1]
	x = 1
	for i in month_days:
		x += i
		array.append(x)
	return (array)

import calendar

count = 0 #count each Sunday == 1st month
y = 6 #1st Jan 1901 was a Tuesday, so Sunday was 6th. 'y' will change for each year.
for year in range(1901,2001):
	if calendar.isleap(year) == True:
		month_days[1] = 29 #allocate 29 days to Feb
		firsts = firsts_of_month(month_days) #calculate list of 1st days based on Feb change
		for b in range(y,367,7): #iterate through Sundays
			for a in firsts: #iterate through first days
				if a == b:
					count += 1
			if b >= 360:
				y = b - 359 #leap year formula to get next year's first Sunday
				
	else:
		month_days[1] = 28 #allocate 28 days to Feb
		firsts = firsts_of_month(month_days) #calculate list of 1st days based on Feb change
		for b in range(y,366,7): #iterate through Sundays
			for a in firsts: #iterate through first days
				if a == b:
					count += 1
			if b >= 359:
				y = b - 358 #non-leap year formula to get next year's first Sunday
print (count)