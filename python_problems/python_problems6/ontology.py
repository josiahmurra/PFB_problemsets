#!/usr/bin/env python3

# import tsv files as sets
with open('ferret_all_genes.tsv', 'r') as all_genes_obj:

    all_genes = set()

    for line in all_genes_obj:

        line = line.rstrip()

        if line[0] == 'E':
            all_genes.add(line)

with open('ferret_stemcellproliferation_genes.tsv', 'r') as stem_genes_obj:

    stem_genes = set()

    for line in stem_genes_obj:

        line = line.rstrip()

        if line[0] == 'E':
            stem_genes.add(line)

with open('ferret_pigmentation_genes.tsv', 'r') as pig_genes_obj:

    pig_genes = set()

    for line in pig_genes_obj:

        line = line.rstrip()

        if line[0] == 'E':
            pig_genes.add(line)

with open('ferret_txnfactor_genes.tsv', 'r') as tf_genes_obj:

    tf_genes = set()

    for line in tf_genes_obj:

        line = line.rstrip()

        if line[0] == 'E':
            tf_genes.add(line)


not_stem = all_genes.difference(stem_genes)

pig_stem = stem_genes.intersection(pig_genes) # both stem and pigment

tf_stem = tf_genes.intersection(stem_genes)

print(f'{tf_stem}')
