#!/usr/bin/env python3

import random


my_seq = 'ATGCCCGGCCCGGC' 


my_list = list(my_seq) #strings are immutable so need to get a list


for n in range(len(my_seq)):
    # using randrange from random module to get random values from a range
    start_range = random.randrange(0,len(my_list))
    end_range = random.randrange(0, len(my_list))

    # need to get the values at each random index position
    start_value = my_list[start_range]
    end_value = my_list[end_range]

    # don't want to modify the original list
    tmp_list = my_list.copy() #create a copy of my_seq

    # swap the values
    tmp_list[start_range] = end_value
    tmp_list[end_range] = start_value

    print(f'swapped {start_range} with {end_range} to get {tmp_list}')
