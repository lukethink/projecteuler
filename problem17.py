"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

"""

"""
My observations:

Unique letter counts are only for numbers 1-20, 30, 40, 50, 60, 70, 80, 90 and the hundreds, up to 1000.
All other numbers are combinations of these.
If can work out total of first 99, then next hundred is the same with 100 x 'onehundred' added to the total.
"""

one_to_nine = len('one') + len('two') + len('three') + len('four') + len('five') + len('six') + len('seven') + len('eight') + len('nine')

ten_to_nineteen = len('ten') + len('eleven') + len('twelve') + len('thirteen') + len('fourteen') + len('fifteen') + len('sixteen') + len('seventeen') + len('eighteen') + len('nineteen')

twenty_to_ninetynine = (8*one_to_nine) + 10*(len('twenty') + len('thirty') + len('forty') + len('fifty') + len('sixty') + len('seventy') + len('eighty') + len('ninety'))

hundreds = 900*(len('hundred')) + 100*one_to_nine

ands = len('and') * (99 * 9)

all_to_onethousand =  10*(one_to_nine + ten_to_nineteen + twenty_to_ninetynine) + hundreds + ands + len('onethousand')
print (all_to_onethousand)