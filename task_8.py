def fact2(n):
    if n <= 0:
        return 1
    else:
        return n * fact2(n - 2)

#--------------------------------------------

ls = ['dfbjjd','kapak','tenet']
def palindrom(word):
    for i in word:
        if i[::-1] == i[:]:
            print(f'Данное слово является палиндромом: {i}')
#------------------------------------------------

import math
def sin1 (x, e):
    if abs(x) > e:
        print(math.sin(x))