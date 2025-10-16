#!/usr/bin/env python3

import sys

my_dat = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

my_dat.sort(key=len, reverse=True)

i = 0
for n in my_dat:
    print(i, len(n), n, sep='\t')
    i += 1

