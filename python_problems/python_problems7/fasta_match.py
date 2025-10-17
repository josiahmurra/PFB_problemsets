#!/usr/bin/env python3

import re

fasta_dir = 'Python_07.fasta'


with open(fasta_dir, 'r') as fasta_obj:

    n = 1
    fasta_dic = {} # initialize a dictionary

    for line in fasta_obj:

        line
        
        found = re.search(r'^>(\S+)\s(.+)', line)

        if found:

            header = found.group(1) # give a name for the sequence
            my_seq = '' # reset sequence if your starting to have a new header

            print(f'The header at line {n} is')
            print(f'id:{found.group(1)}')
            print(f'desc:{found.group(2)}\n')

        else:

            my_seq = my_seq + line # join current line with previous sequence lines

            fasta_dic[header] = my_seq

        n += 1


print(fasta_dic)

