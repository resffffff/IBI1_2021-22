import re
gene ='ATGCAATCGACTACGATCAATCGAGGGCC'  # Now the 'gene' is defined and read as a sequence
gene_seq = re.findall(r'GAATTC', gene)  # We create a gene list to count the appearing times of 'GAATTC'
print(len(gene_seq) + 1)   # We print out the amount of gene that containing the specific gene segment.

