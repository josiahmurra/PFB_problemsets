#!/usr/bin/env python3

import sys
# code for calculating a factorial
# i=10
# x=1

# while i > 0:
#     x = x * i
#     print(i)
#     i -= 1
    

# print(x)

# code for calculating sums of odds and evens
# my_list = [101,2,15,22,95,33,2,27,72,15,52]

# my_list.sort()
# even = 0
# odd = 0

# for n in my_list:
#     if n % 2 == 0:
#         even = even + n
#         print(n, "is even")
#     else:
#         odd = odd + n
#         print(n, "is odd")

# print(f'Sum of even numbers: {even}')
# print(f'Sum of odds: {odd}')

# Two ways of creating lists:
#my_list = [0 + i for i in range(100)] # with list comprehension
#my_list2 = [1 + i for i in range(100)]
#my_list3 = list(range(1, 101)) # with the list function

user_input = int(sys.argv[1])
my_list4 = [1 + i for i in range(user_input)]


print(my_list4)

