#!/usr/bin/env python3

import sys

fasta_path = 'Python_06.fasta'
fasta_dic = {}

with open(fasta_path, 'r') as fasta_obj:

    # First line of fasta is seq name and Second line is sequence
    # We want to create a dictionary of fasta sequences
    n = 0

    for line in fasta_obj:

        line = line.rstrip().replace(">", "")

        if n % 2 == 0:
            my_key = line # First line is the key. Not sure if fasta files ever have headers?
        elif n % 2 == 1:
            fasta_dic[my_key] = line # Second line is the value
        n += 1

print(fasta_dic)






