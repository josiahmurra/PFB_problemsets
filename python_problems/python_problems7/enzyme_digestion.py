#!/usr/bin/env python3

import sys
import re

enz_dir = 'test_enzymes.txt'
usr_enz = sys.argv[1]
fasta_dir = sys.argv[2]

with open(enz_dir, 'r') as enzyme_obj:

    n=0

    split_pattern = r'  +'
    enzyme_dic = {}

    # read enzymes info into python
    for line in enzyme_obj:

        line = line.rstrip()

        if n > 9: # skip the header

            split_line = re.split(split_pattern, line)

            enzymes = split_line[0].split(" ")

            for enz in enzymes: # each enzyme has two names

                enz = re.sub(r'[(|)]', '', enz)

                enzyme_dic[enz] = split_line[1]

        n += 1


cut_site = enzyme_dic[usr_enz] # retrieve the cutsite from dictionary

cut_pattern = cut_site.replace('^', '') # remove carrot for pattern matching

# open fasta file and search for cut site
with open(fasta_dir, 'r') as fasta_obj:

    for line in fasta_obj:

        line = line.rstrip()

        if re.search(cut_pattern, line):

            marked_line = re.sub(cut_pattern, cut_site, line)

            fragments = re.split(r'\^', marked_line)

            fragments.sort(key=len, reverse=True)

            print(fragments)






