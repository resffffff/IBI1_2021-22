a=19245301 # the number of cases of in 2022
b=4218520 # the number of cases in 2021
c=271 # the number of cases in 2020
d=b-c
e=a-b
#print(d-e)
#print(d,e)
if a>b and a>c:
    print("COVID cases in 2022 is the biggest.")
if b>a and b>c:
    print("COVID cases in 2021 is the biggest.")
if c>a and c>b:
    print("COVID cases in 2020 is the biggest.")
# comment: We can find that COVID cases in 2022 is the biggest.
X = input('Input: The value of x is:')# input a boolean variable X
Y = input('Input: The value of y is:')# input a boolean variable Y
W = X and Y
print(W) # output W


