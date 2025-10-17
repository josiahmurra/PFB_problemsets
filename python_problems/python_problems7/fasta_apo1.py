#!/usr/bin/env python3

import re

fasta_dir = 'Python_07_Apo1.fasta'

#fasta_dir = 'test.fasta'


with open(fasta_dir, 'r') as fasta_obj:

    n = 1
    fasta_dic = {} # initialize a dictionary

    for line in fasta_obj:

        line = line.strip()
        
        found = re.search(r'^>(\S+)\s?(.+)?', line)

        if found:

            header = found.group(1) # give a name for the sequence
            my_seq = '' # reset sequence if your starting to have a new header

            #print(f'The header at line {n} is')
            #print(f'id:{found.group(1)}')
            #print(f'desc:{found.group(2)}\n')

        else:

            my_seq = my_seq + line # join current line with previous sequence lines

            fasta_dic[header] = my_seq

        n += 1


print(f'This fasta has {len(fasta_dic)} sequence(s)')

#print(fasta_dic)

# Iterate through the fasta dictionary to search for cut sites
cut_for = '[AG]AATT[CT]' # apo1 recognition sequence as re

for sequence in fasta_dic:

    found = re.sub(r'([AG])AATT([CT])', r'\1^AATT\2', fasta_dic[sequence]) # mark cut site

    if re.search(r'^', found): # check if a substitution was made

        #print(f"Sequence {sequence} was cut.")

        fragments = found.split("^")

        fragments.sort(key=len, reverse=True)

        print(fragments)



            


