import re
gene_names = []
genes_seq = []
gene = open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
gene = gene.read()  # Now the 'gene' is opened and read as a sequence
re.sub('\n', '', gene)
gene_seq = re.findall(r'GAATTC', gene)  # We create a gene list containing 'GAATTC'
print(len(gene_seq) + 1)   # We print out the amount of gene that containing the specific gene segment.

