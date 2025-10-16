#!/usr/bin/env python3

# create file handle
text_handle = open('Python_06.txt', mode="r")

#print(text_handle.read().replace('\n', ' '))


with open('Python_06.txt', "r") as text_handle, open('Python_06_uc.txt', 'w') as out_handle:
    for line in text_handle:
        line = line.upper()
        
        out_handle.write(f'{line}')

