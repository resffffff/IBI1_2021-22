(money,price) = input('write the money you take:\n'),input('write the price:\n')
def calculate(money,price):
    #if price == int and money == int:
        #error = False
        piece = 0
        while int(piece)*int(price) <= int(money):
            piece += 1
        else:
            change = int(money) - (int(piece) - 1)*int(price)
            piece -= 1
            return piece, change
    #else:
        #error = True
        #print('your input is not an int!')
print('User can afford ' + str(calculate(money,price)[0]) + ' piece(s) of chocolate bar\nAnd the change is ' + str(calculate(money,price)[1]))