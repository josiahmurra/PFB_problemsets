#!/usr/bin/env python3

import sys

my_number = sys.argv[1]
my_float = float(my_number)
my_num_pos = (my_float>0) - (my_float<0)
my_num_50 = (my_float>50) - (my_float<50)

print('The number:', my_float, 'is being evaluated')

if (my_float % 2) == 0:
    print('Number is even')
else:
    print('Number is odd')

if my_num_pos == 0:
    print('and equals zero')
elif my_num_pos == 1:
    print('and is positive')
elif my_num_pos == -1:
    print("and is negative")

if my_num_50 == 1:
    print('and greater than 50')
    if (my_float % 3) == 0:
        print('and is divisible by 3')
elif my_num_50 == -1:
    print('and less than 50')
elif my_num_50 == 0:
    print('and equals 50')