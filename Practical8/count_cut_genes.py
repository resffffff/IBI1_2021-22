f=open("C:/Users/xzy/IBI1_2021-22/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
fout1 = open('C:/Users/xzy/IBI1_2021-22/Practical8/countgene.fa','w')
EcoRI='GAATTC'
gene_order=0
seqs=[]
list_name=[]
for line in f:
    if line.startswith('>'):
        list_name.append(line)
        gene_order=gene_order+1
    if (line.startswith('>'))and (gene_order!=1):
        sum_1 = ''
        for seq in seqs:
            sum_1 = sum_1 + str(seq)
        sum_1 = sum_1.upper()
        seqs=[]
        i=0
        count=0
        while (i<=len(sum_1)-5) :
            i=i+1
            if sum_1[i:i+6]==EcoRI:
                count=count+1
                name_now=list_name[gene_order-2]
                #print(name_now[0:8],"        ",len(sum_1))
                #print(sum_1)
        if count!=0:
            info1=str(name_now[0:8])+str("        ")+str(count+1)+"\n"
            info2=str(sum_1)+"\n"
            fout1.write(info1)
            fout1.write(info2)
            #print(name_now[0:8], "        ", count+1)
            #print(sum_1)
    if not line.startswith('>'):
        seqs.append(line.replace('\n',''))
f.close()
fout1.close()