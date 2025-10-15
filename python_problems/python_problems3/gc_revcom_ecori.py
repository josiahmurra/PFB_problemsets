#!/usr/bin/env python3

# Load modules
import sys

# get system argument and asign as my_sequence
my_sequence = sys.argv[1]

#my_sequence = str(my_sequence)

# convert sequence to uppercase
my_sequence_upper = my_sequence.upper()

# print position 100-200 (101 nucleotides)
#my_sequence = my_sequence[99:200]


# count A T C and G
n_count = len(my_sequence_upper)
a_count = my_sequence_upper.count('A')
t_count = my_sequence_upper.count('T')
c_count = my_sequence_upper.count('C')
g_count = my_sequence_upper.count('G')

# print nucleotide composition to screen
print(f"""Sequence composition:
      {n_count} total nucleotides
      {a_count} 'A' nucleotides ({a_count/n_count:.3%})
      {t_count} 'T' nucleotides ({t_count/n_count:.3%})
      {c_count} 'C' nucleotides ({c_count/n_count:.3%})
      {g_count} 'G' nucleotides ({g_count/n_count:.3%}) 
      'GC' content is {(c_count+g_count)/n_count:.3%}""")

# convert 'T' to 'U' (for RNA sequence)
my_rna = my_sequence.replace('T', 'U')


# Code for getting reverse compliment sequence:
# reverse the original input
my_reverse = my_sequence[::-1]

# get the complimentary sequence
# 1 - Create a code of original sequences and a key of their reverse sequences
my_nucleotides = ['A', 'T', 'C', 'G', 'a', 't', 'c', 'g']
my_nucleotides_key = ['T', 'A', 'G', 'C', 't', 'a', 'g', 'c']

# 2 - Initialize the rev_C
my_rev_com = my_reverse # start with the reverse sequence

n = 1
for nucleotide in my_nucleotides:
    my_rev_com = my_rev_com.replace(nucleotide, str(n))
    n += 1

n = 1 # reset n
for nucleotide in my_nucleotides_key:
    my_rev_com = my_rev_com.replace(str(n), nucleotide)
    n += 1

print(my_rev_com)


# Get EcoRI Enzyme cutsite positions
# define EcoRI recognition sites
eco_for = 'GAATTC'
eco_rev_com = 'GAATTC'

# get the index of positions
for_start_cut = my_sequence_upper.find(eco_for)
rev_start_cut = my_rev_com.upper().find(eco_rev_com)


# print the cut sites
print(f"""EcoRI Digestion Info:
Forward Stand: startPos={for_start_cut+1} endPos={for_start_cut+7}
Reverse Strand: startPos={rev_start_cut+1} endPos={rev_start_cut+7}""")