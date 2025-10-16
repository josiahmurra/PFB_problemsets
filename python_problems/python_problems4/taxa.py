#!/usr/bin/env python3

taxa_string = 'sapiens : erectus : neanderthalensis'
print(type(taxa_string))
print(taxa_string)

# create taxa list
taxa_list = taxa_string.split(':')
print(taxa_list)

# sort taxa list alphanmerically
taxa_list.sort()
print(taxa_list)

# sort taxa list by string length
taxa_list.sort(key=len, reverse = False)
print(taxa_list)