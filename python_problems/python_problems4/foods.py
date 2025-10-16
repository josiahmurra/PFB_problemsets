#!/usr/bin/env python3

my_favs = ['chocolate', 'paneer', 'pork', 'basque cheesecake', 'siracha']

# These two pieces of code are functionally equivalent
my_favs[2:3] = ['bacon']
my_favs[2] = 'bacon'

my_favs.append('momos') # I don't need to reasign this list in order to modify it

my_favs.insert(0, 'tacos') # Remember to use 0 if you want something up front

my_favs.pop(2) # This removes index 2 from the list

print('_'.join(my_favs))

