#!/usr/bin/env python3

# import tsv files as sets
with open('ferret_all_genes.tsv', 'r') as all_genes_obj:

    all_genes = set()

    for line in all_genes_obj:

        line = line.rstrip()

        all_genes.add(line)

with open('ferret_stemcellproliferation_genes.tsv', 'r') as stem_genes_obj:

    stem_genes = set()

    for lines in stem_genes_obj:

        line = line.rstrip()

        if line[0] == 'E':
            stem_genes.add(line)

with open('ferret_pigmentation_genes.tsv', 'r') as pig_genes_obj:

    pig_genes = set()

    for lines in pig_genes_obj:

        line = line.rstrip()

        pig_genes.add(line)

print(pig_genes.intersection(stem_genes))
