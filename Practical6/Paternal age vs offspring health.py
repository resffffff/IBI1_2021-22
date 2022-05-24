# Pseudocode:
# input the paternal_age data list and the chd data list
# create the dictionary
# invoke plt.scatter to create a plot
# set the marker, colour and size of the dots
# output the plot
# input the father's age
# use while loop to find CHD in 'chd' list
# output the CHD risk in the offspring
import numpy as np
import matplotlib.pyplot as plt

paternal_age = [30,35,40,45,50,55,60,65,70,75] # create a list containing paternal ages
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
# creat the dictionary
dictionary = dict(zip(paternal_age,chd)) # Output a dictionary containing relative informations in the 2 list
print(dictionary)
plt.scatter(list(dictionary.keys()),list(dictionary.values()),
        marker = 'o',
        c = 'red', # the colour of dots are set as red
        s = 50 # the radius of the dot is set as 100
            ) # create a scatter plot
plt.title("the effect of paternal age on offspring health")
plt.xlabel("Paternal age")
plt.ylabel("chilrden's health")
plt.show()
#now it will function correctly and output a plot with keys and values.
age = int(input('Input the age of father:'))
i = 0
while True:
    if paternal_age[i] == age:
        print('When the father is',age, ', the risk of CHD in the offspring is', chd[i])
        break
    i += 1
    if i > 10: # the loop will repeat for 10 times
        break

