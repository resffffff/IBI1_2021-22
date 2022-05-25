from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import re
import numpy as np
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
childnodes={}
#First
print("There are ",len(terms)," terms in the file.")

for term in terms:
    l=0
    adder=[]
    id= term.getElementsByTagName('id')[0].childNodes[0].data
    for i in term.getElementsByTagName('is_a'):
        adder.append(term.getElementsByTagName('is_a')[l].childNodes[0].data)
        l=l+1
    childnodes[id] = adder
#create a dictionary called childnodes recording all ids of terms and their "is_a"s' id.

v={}
for i in childnodes:
    v[i]=0

new_dic={}
timer=0
for i in childnodes:
    new_dic[i]=[]


timer=0


def loop(a):
    new_dic[m] += childnodes[a]
    if len(childnodes[a])!=0:
        for x in childnodes[a]:
            loop(x)
#Reverse the dictionary to get a dictionary filled with key of terms, and values of parentnodes

for m in childnodes.keys():
    loop(m)

for i in new_dic:
    new_dic[i]=list(set(new_dic[i]))
for i in new_dic:
    for j in new_dic[i]:
        v[j]+=1
values=[]
#Delete repeated values of parentnodes and calculate numbers of childnodes

for i in v:
    values.append(v[i])
translation=[]

#distribution of child nodes in the Go
plt.boxplot(values,
            )
plt.title("Distribution of childnodes in the GO.xml")
plt.ylabel("Number of Childnodes")
plt.show()

#Distribution of child nodes in the GO associated with translation
for term in terms:
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    defi = term.getElementsByTagName('def')[0]
    defstr=defi.getElementsByTagName('defstr')[0].childNodes[0].data
    if defstr.find("translation")>=0:
        translation.append(v[id])

plt.boxplot(translation,
            )
plt.title("Distribution of child nodes from terms associated with translation")
plt.ylabel("Childnodes")
plt.show()

print("The average of childnodes of all terms")
print(np.average(values))
print("The average of childnodes of terms associated with translation")
print(np.average(translation))
#COMMENT: The average of child nodes associated with translationis bigger than that of overall terms.