#!/usr/bin/env python3

import sys

favorites = {
    'book' : 'bruchko',
    'song' : 'baseball - hippocampus',
    'tree' : 'mango'
}

favorites['organism'] = 'bug' # add a new key : value to dictionary

#print(f'Select category ({favorites.keys()})')
print(f'What is your favorite {sys.argv[1]}?')

x = input()

favorites[sys.argv[1]] = x


print(f'Your favorite {sys.argv[1]} is stored as {favorites[sys.argv[1]]}')

