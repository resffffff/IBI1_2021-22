import re
edit_distance = 0
seq1 = (open(r'DLX5_human.fa','r')).read()
seq1 = re.sub(r'\n', '',seq1)
seq11 = re.findall(r'[)](.*)',seq1,re.S)
seq2 = (open(r'DLX5_mouse.fa','r')).read()
seq2 = re.sub(r'\n', '',seq2)
seq21 = re.findall(r'[)]\s(.*)',seq2,re.S)
seq_ram = (open(r'RandomSeq.fa','r')).read()
seq_ram = re.sub(r'\n', '',seq_ram)
seq_ram1 = re.findall(r'q(.*)',seq_ram,re.S)
seq11 = ''.join(seq11)
seq21 = ''.join(seq21)
seq_ram1 = ''.join(seq_ram1)
#print(len(seq_ram1),len(seq11),len(seq21))
for i in range(len(seq11)):
    if seq11[i] != seq_ram1[i]:
        edit_distance += 1
print('The human-random distance is ' + str(edit_distance))
edit_distance = 0
for i in range(len(seq21)):
    if seq21[i] != seq_ram1[i]:
        edit_distance += 1
print('The mouse-random distance is ' + str(edit_distance))
edit_distance = 0
for i in range(len(seq11)):
    if seq11[i] != seq21[i]:
        edit_distance += 1
print('The human-mouse distance is ' + str(edit_distance))