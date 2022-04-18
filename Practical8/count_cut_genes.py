import re
gene11 = []
gene = open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
gene = gene.read()  # open the fa file
for list in gene:
    list = list.strip(r'\n')
gene1 = gene.split('>') # create a list for each DNA sequence
for i in range(len(gene1)):
    if'GAATTC' in gene1[i]:
        gene11.append(re.sub(r'\n', '', gene1[i]))
a = re.compile(r'gene:(.*?)gene.*?](.*?)>', re.S)
gene_seq = a.findall(gene)
b = input('write your file name:\n') # name the file that you want to create
x = open('%s.fa' % b, 'w')  # then operating on the new file created by users
for i in range(len(gene_seq)):
    re.sub(r'\n', '', gene_seq[i][1])
    x.write('>' + gene_seq[i][0] + '           ' + str(len(gene_seq[i][1]) + 1) + '\n' + gene_seq[i][1])
    print(gene_seq[i][0] + 'is loaded') # extract the gene name and sequence into the file
x.close()