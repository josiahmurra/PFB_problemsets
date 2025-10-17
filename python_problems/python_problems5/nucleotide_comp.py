#!/usr/bin/env python3

import sys

seq_path = 'Python_06.seq.txt'

with open(seq_path, 'r') as seq_obj:

    # First line of fasta is seq name and Second line is sequence
    # We want to create a dictionary of fasta sequences
    n = 0
    
    for line in seq_obj:

        line = line.rstrip() # remove any trailing whitespace
        line_ls = line.split('\t') # split the line into name and sequence
        line_seq = line_ls[1] # get the sequence
        seq_len = len(line_seq) # get the sequence length

        nt_dic = {} # initialize a dictionary for this line

        for nt in set(line_seq): # get unique nucleotides using set()

            nt_dic[nt] = line_seq.count(nt) # count the n for each nucleotide

        print(f'Name\t{line_ls[0]}')
        print(f'Length\t{seq_len}')

        for key in sorted(nt_dic.keys()):
            print(f'{key}\t{nt_dic[key]}')

        print(f'GC\t{(nt_dic['G']+nt_dic['C'])/seq_len:.2%}')
                





