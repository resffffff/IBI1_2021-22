# The blosum 62 matrix is scored by comparing the amino acid in two seqs
# Input the file containing the AA sequence
# calculate the amino acid similarity and the score
import re

amino_acid = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
              'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V',
              'B', 'Z', 'X']
matrix = [
         [4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2, -1, 1, 0, -3, -2, 0, -2, -1, 0],
         [-1, 5, 0, -2, -3, 1, 0, -2, 0, -3, -2, 2, -1, -3, -2, -1, -1, -3, -2, -3, -1, 0, -1],
         [-2, 0, 6, 1, -3, 0, 0, 0, 1, -3, -3, 0, -2, -3, -2, 1, 0, -4, -2, -3, 3, 0, -1],
         [-2, -2, 1, 6, -3, 0, 2, -1, -1, -3, -4, -1, -3, -3, -1, 0, -1, -4, -3, -3, 4, 1, -1],
         [0, -3, -3, -3, 9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2],
         [-1, 1, 0, 0, -3, 5, 2, -2, 0, -3, -2, 1, 0, -3, -1, 0, -1, -2, -1, -2, 0, 3, -1],
         [-1, 0, 0, 2, -4, 2, 5, -2, 0, -3, -3, 1, -2, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1],
         [0, -2, 0, -1, -3, -2, -2, 6, -2, -4, -4, -2, -3, -3, -2, 0, -2, -2, -3, -3, -1, -2, -1],
         [-2, 0, 1, -1, -3, 0, 0, -2, 8, -3, -3, -1, -2, -1, -2, -1, -2, -2, 2, -3, 0, 0, -1],
         [-1, -3, -3, -3, -1, -3, -3, -4, -3, 4, 2, -3, 1, 0, -3, -2, -1, -3, -1, 3, -3, -3, -1],
         [-1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4, -2, 2, 0, -3, -2, -1, -2, -1, 1, -4, -3, -1],
         [-1, 2, 0, -1, -3, 1, 1, -2, -1, -3, -2, 5, -1, -3, -1, 0, -1, -3, -2, -2, 0, 1, -1],
         [-1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5, 0, -2, -1, -1, -1, -1, 1, -3, -1, -1],
         [-2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0, -3, 0, 6, -4, -2, -2, 1, 3, -1, -3, -3, -1],
         [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7, -1, -1, -4, -3, -2, -2, -1, -2],
         [1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1, 4, 1, -3, -2, -2, 0, 0, 0],
         [0, -1, 0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1, 1, 5, -2, -2, 0, -1, -1, 0],
         [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11, 2, -3, -4, -3, -2],
         [-2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1, -2, -1, 3, -3, -2, -2, 2, 7, -1, -3, -2, -1],
         [0, -3, -3, -3, -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4, -3, -2, -1],
         [-2, -1, 3, 4, -3, 0, 1, -1, 0, -3, -4, 0, -3, -3, -2, 0, -1, -4, -3, -3, 4, 1, -1],
         [-1, 0, 0, 1, -3, 3, 4, -2, 0, -3, -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1],
         [0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, 0, 0, -2, -1, -1, -1, -1, -1]]

seq1 = (open(r'DLX5_human.fa','r')).read()
seq1 = re.sub(r'\n', '',seq1)
seq_human = re.findall(r'[)](.*)',seq1,re.S)
seq_mouse = (open(r'DLX5_mouse.fa','r')).read()
seq_mouse = re.sub(r'\n', '',seq_mouse)
seq_mouse = re.findall(r'[)]\s(.*)',seq_mouse,re.S)
seq_ram = (open(r'RandomSeq.fa','r')).read()
seq_ram = re.sub(r'\n', '',seq_ram)
seq_ram = re.findall(r'q(.*)',seq_ram,re.S)
seq_human = ''.join(seq_human)
seq_mouse = ''.join(seq_mouse)
seq_ram = ''.join(seq_ram)
# print(len(seq_ram1),len(seq11),len(seq21))
# print(seq_mouse)
# print(seq_ram)
# print(seq_human)

def BLOSUM(seq1,seq2):
    score = 0
    for i in range(len(seq1)):
        score += matrix[amino_acid.index(seq1[i])][amino_acid.index(seq2[i])]
    return score

def percentage(seq1,seq2):
    AA = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            AA += 1
    per_AA = AA / (len(seq1))
    return per_AA


print('the percentage of identical	amino acids for human and random_seq is',percentage(seq_human,seq_ram))
print('the percentage of identical	amino acids for mouse and random_seq is',percentage(seq_mouse,seq_ram))
print('the percentage of identical	amino acids for human and mouse is',percentage(seq_human,seq_mouse))
print('the BLOSUM score for human and random is',BLOSUM(seq_human,seq_ram))
print('the BLOSUM score for mouse and random_seq is',BLOSUM(seq_mouse,seq_ram))
print('the BLOSUM score for human and mouse is',BLOSUM(seq_human,seq_mouse))
print("Comments: from blosum score we can see that the amino acids score for human and mouse is quite high, and the percentage of identical amino acids for human and mouse is 96.5%.\nIt can serve as an evidence to support Darvin's theory of evolution. All animals came from the same ancestor. Although we are not like the mouse totally, we can still share the similar coding genes. It is quite miracle. " )
#comments:
# from blosum score we can see that the amino acids score for human and mouse is quite high, and the percentage of identical amino acids for human and mouse is 96.5%.
# It can serve as an evidence to support Darvin's theory of evolution. All animals came from the same ancestor. Although we are not like the mouse totally, we can still share the similar coding genes. It is quite miracle.