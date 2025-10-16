#!/usr/bin/env python3

import sys

ex_fastq = '''@SEQ_ID  
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT  
+  
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65  '''


with open(sys.argv[1], 'r') as seq_obj:

    # Variables for counting
    line_n = 0
    seq_n = 0
    char_n = 0
    nt_n = 0

    # Every fastq has 4 lines per entry... so if the line 'n' % 4 = 0 this is the SEQ_ID
    for line in seq_obj:

        line = line.rstrip() # remove any new line characters

        line_length = len(line) # get line length

        char_n = char_n + line_length # count characters per line

        if line_n % 4 == 0:
            seq_n += 1 # count the number of sequences
        elif line_n % 4 == 1:
            nt_n = nt_n + line_length # count the number of nucleotides

        line_n += 1 # increment line counter

    print(f'''Number of lines is {line_n}
    Number of Sequences is {seq_n}
    Number of Characters is {char_n}
    Number of Nucleotides is {nt_n}
    Average line length is {char_n / line_n}
    Average Sequence Length is {nt_n / seq_n}''')
    