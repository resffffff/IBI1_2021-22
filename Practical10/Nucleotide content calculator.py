seq = input('write your DNA sequence:\n')
def calculate(nucleotide):
    A = 0
    T = 0
    C = 0
    G = 0
    # seq = input('write your DNA sequence:\n')
    for i in range(0,len(seq)):
        if seq[i] == ('A' or 'a'):
            A += 1
        elif seq[i] == ('T' or 't'):
            T += 1
        elif seq[i] == ('C' or 'c'):
            C += 1
        elif seq[i] == ('G' or 'g'):
            G += 1
    def percent(a):
        percent_ = str(a/(len(seq)))
        return percent_

    A_ = percent(A)
    T_ = percent(T)
    C_ = percent(C)
    G_ = percent(G)
    print('When sequence is '+seq + ':\n'
          + 'The percent of A is ' + A_ + '\n'
          + 'The percent of T is ' + T_ + '\n'
          + 'The percent of C is ' + C_ + '\n'
          + 'The percent of G is ' + G_ + '\n')
calculate(seq)

seq = 'GTTgtgtgACC'    # Here used as an example.
calculate(seq)
print("The second output is the example. The first output is the result of your input")