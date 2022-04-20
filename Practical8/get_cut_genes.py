import re
gene_types = []
gene_list1 = []
gene = open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
gene = gene.read()   # load the origen file
gene_list = gene.split('>')    # identify the gene by '>'
for i in range(len(gene_list)):
    if 'GTTAAC' in gene_list[i]:   # input sequences that possessing 'GTTAAC' in the list
        gene_list1.append(gene_list)    # input the sequences in a new list
gene1 = open(r'cut_genes.fa', 'w')
gene_types = re.compile(r'gene:(.*?)gene.*?](.*?)[ATCG]', re.S)   # use 正则表达式 to obtain the gene name and sequence
gene_names1 = gene_types.findall(gene)
for i in range(len(gene_names1)):
    gene1.write('Gene: ' +  gene_names1[i][0] + '      count: ' + str(len(gene_names1[i][1])) + '\n')
    print(gene_names1[i][0] + ' has finished')
gene1.closed
print('The total number of DNA seq is ' + str(len(gene_names1)))





