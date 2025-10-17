#!/usr/bin/env python3

# load re module
import re

text_handle = 'Python_07_nobody.txt'


with open(text_handle, 'r') as text_obj, open('Micah.txt', 'w') as out_obj:

    n = 1

    for line in text_obj:

        #my_match = re.finditer('Nobody', line, re.IGNORECASE)

        new_line = re.sub('Nobody', 'Micah', line, re.IGNORECASE)

        out_obj.write(new_line)

        n += 1

        



