#     create a dictionary firstly, and then create the plot using "plt.scatter"
import numpy as np
import matplotlib.pyplot as plt

AGE = [30,35,40,45,50,55,60,65,70,75]
HEALTH = [1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
dictionary = {'30': 1.03,'35': 1.07,'40': 1.11,'45': 1.17,'50': 1.23,'55': 1.32,'60': 1.42,'65': 1.55,'70': 1.72,'75':1.94}
print(dictionary) #Output a	dictionary in python containing the	information	in the two lists above
plt.scatter(list(dictionary.keys()),list(dictionary.values()))
plt.xlabel("Paternal age")
plt.ylabel("chilrden's health")
plt.show()
#now it will function correctly and output a plot with keys and values.   