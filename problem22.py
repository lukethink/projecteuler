"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

# open the file and turn the data into an alphabetically sorted list
with open('c:\\users\luke\desktop\p022_names.txt','r') as textfile:
	names = textfile.read() # copies the file data to a variable
	stripped = names.strip('"') # removes the " at beginning and end of file
	names_list = stripped.split('","') # creates a list from the data
	names_list.sort() # sorts the list alphabetically

# create a dictionary that gives each letter of the alphabet its appropriate score
import string
az_dict = {}
x = 1
for i in string.ascii_uppercase:
	az_dict[i] = x
	x += 1

# create a function that returns the relevant score for any uppercase letter
def letter_score(letter):
	score = az_dict[letter]
	return score

# create a function that returns the alphabetical value of a name
def name_value(name):
	value = 0
	for j in name:
		value += letter_score(j)
	return value

# create code that returns the result of alphabetical value * alphabetical position
total = 0
for k in names_list:
	total += ( name_value(k) * (names_list.index(k)+1) )
print (total)