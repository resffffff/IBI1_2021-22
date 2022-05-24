# What does this piece of code do?
# Answer: this program generates a randon number ten times but only print the last one.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
# The while loop will repeat 10 times to create a random integer in range from 1 to 100.
while progress<10:
	progress+=1
	n = randint(1,100)

# print the last n
print(n)

# output just one random integer ranging from 1 to 100.