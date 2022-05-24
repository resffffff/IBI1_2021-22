# pseudocode:
# began with no cut
# if the pieces are less than we need:
# continue cutting. n is added up.
# when the pieces are larger than we need:
# stop the program
# output the cutting times and the cutting pieces
n = 0
p = 0
while p < 64:  # If the total is still less than 64
    n = n + 1
    p = (n * n + n + 2) / 2
else:
    print("The cutting times are " + str(n) + " and the final cutting pieces are " + str(p))
#we can get the cutting times and slices

