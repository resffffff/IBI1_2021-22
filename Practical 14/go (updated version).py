import re
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt
DOMtree = xml.dom.minidom.parse('go_obo.xml')
# open and read the files by parse
collections = DOMtree.documentElement
terms = collections.getElementsByTagName('term')
print("The total number of terms is",len(terms))
child_nodes = 0
dict1 = {}
defstr_id = []
values1 = []
value = {}
dict1 = {}
new_dic = {}
is_list = []
for term in terms:
    n = 0
    m = 0
    box = []
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    is_list = term.getElementsByTagName('is_a')
    for i in range(len(is_list)):
        box.append(is_list[i].childNodes[0].data)
    dict1[id] = box
 # obtain a loop dictionary including the dictionary of the id and its "is_a"
for i in dict1:
    value[i] = 0

for i in dict1:
    new_dic[i] = []
def recursion(a):  # This function is to find the childnodes from parentnodes and parent_childnodes
    new_dic[h] += dict1[a]
    if len(dict1[a]) != 0:
        for x in dict1[a]:
            recursion(x)
dict_keys1 = []
dict_keys = []
for key in dict1.keys():
    dict_keys.append(key) # I find there is some unexpected error if I directly used the keys of the dictionary, so I added it into another list.
while True:   # vital terms are collected in the list and set properly
    for h in dict_keys:
        recursion(h)
    for i in new_dic:
        new_dic[i] = list(set(new_dic[i]))
    for i in new_dic:
        for j in new_dic[i]:
            value[j] += 1
    break
# I find I store the value in a dictionary, so I put it in a list
for i in value:
    values1.append(value[i])
# get the terms containing the tag of the translation, and use values to output a defstr list
value_tran = []
for term in terms:
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    definition = term.getElementsByTagName('def')[0]
    defstr = definition.getElementsByTagName('defstr')[0].childNodes[0].data
    m = re.findall(r'translation',defstr)
    if m != []:
        value_tran.append(value[id])
# then show the two boxplot including all childnodes and
fig = plt.figure(figsize = (15, 5), dpi = 100)  # set the total size and space of the figure
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
plt.subplot(1,2,1)
plt.boxplot(values1, showfliers = True)
plt.title("the distribution of childnodes of go_obo.xml")
plt.ylabel("Childnodes number")

plt.subplot(1,2,2)
plt.boxplot(value_tran, showfliers = True)
plt.title("the distribution of childnodes of go_obo.xml with the tag of translation")
plt.ylabel("Childnodes number")
plt.show()

average1 = sum(values1)/len(values1)
average2 = sum(value_tran)/len(value_tran)
print("the average number of childnotes in all the terms is ",average1)
print("the average number of childnotes in translation terms is ",average2)
if average1 > average2:
    print('The average number of childnotes in all terms is bigger than that in translation terms')
else:
    print('The average number of childnotes in all terms is smaller than that in translation terms')

