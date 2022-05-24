# Pseudocode:
# import pyplot and numpy
# input the score
# make chart

import numpy as np
import matplotlib.pyplot as plt

scores= [45,36,86,57,53,92,65,45]
print(sorted(scores)) # print the score list in which the values are rearranged from low score to high score.
plt.title("A boxplot for Rob's marks") # set the title of the plot
plt.xlabel("Rob") # It is Rob's score
plt.ylabel("marks") # It is a distribution of marks
plt.boxplot(scores,
            vert=True, # make the box vertical
            patch_artist = True # fill the box with colour (blue)
            )
plt.show() # output the boxplot
def mean(score): # this function can calculate the mean of values obtained from a list
    sum = 0
    mean = 0
    for i in range(len(score)): # use a for-loop to sum up the values
        sum += score[i]
    mean = sum/(len(score))
    return mean

if mean(scores) < 60:
    print('Rob failed the ICA')
else:
    print('Rob passed the ICA')
# comment: Rob didn't pass the ICA.