#!/usr/bin/env python3


#test_seq = 'c9\tATCG\nc10\tCTGA'


with open('Python_06.seq.txt', 'r') as seq_obj:

    for line in seq_obj:
       # line = line.rstrip()

        seq_ls = line.split('\t') # split the line

        seq_ls[1] = seq_ls[1].rstrip() # remove new line character

        rev = seq_ls[1][::-1] # reverse sequence
         
        revcom = rev.translate(str.maketrans('ATCG', 'TAGC')) # complement

        print(f'{seq_ls[0]}\t{revcom}') # print line to new file


