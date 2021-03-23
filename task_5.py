while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print((x+y))
        elif s == '-':
            print((x-y))
        elif s == '*':
            print((x*y))
        elif s == '/':
            if y != 0:
                print((x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

#-------------------------------------------------

num = int(input("Введите целое число: "))
sum = 0
mult = 1
while num != 0:
    sum += num % 10
    mult = mult * (num % 10)
    num = num // 10
print("Сумма цифр числа равна: ", sum)
print("Произведение цифр равно: ", mult)

#-------------------------------------------------

f = 0
for ch in range(200, 301):
    if ch != f:
        s1 = 0
        for i in range(1, ch // 2 + 1):
            if ch % i == 0:
                s1 += i
        s2 = 0
        for j in range(1, s1 // 2 + 1):
            if s1 % j == 0:
                s2 += j
        if s2 == ch != s1:
            print(ch, s1)
            f = s1

#-------------------------------------------------
def S(n):
    for i in range(1,n):
        iff = 1/n
        return iff

hre = int(input('enter num:\n'))
print(S(hre))

#-------------------------------------------------
import random
myList = []
a = 0
while a < 19:
    myList.append(random.randint(0,19))
    a += 1
    m = max(myList)
for i in range(0, len(myList), 2):
    myList[i] = m
print(myList)
#-------------------------------------------------

import random
myList = []
a = 0
count = 0
while a < 20:
    myList.append(random.randint(0,20))
    for i in range(0, len(myList)):
        if myList[i] < myList[i+1]:
            count += 1
print(count)
#-------------------------------------------------

from random import randint

matrix1 = []
n = int(input('Enter n:'))
m = int(input('Enter m:'))

matrix = [[randint(1, 9) for j in range(n)] for i in range(m)]
print(*matrix)
for i in range(min(n, m)):
    r = matrix[i].index(max(matrix[i]))
    matrix[i][i], matrix[i][r] = matrix[i][r], matrix[i][i]
print(*matrix)

#-------------------------------------------------

def reverse(lst):
    lis = lst[::-1]
    lis.split(' ')
    return lis


ft = input('enter string\n')
list = str(ft)
print(reverse(list))

#-------------------------------------------------

m = int(input())
n = int(input())
x = range(m,n)
for i in x:
    for e in range(2,i-1):
        if i % e == 0:
            print ("Chislo",i, "Delitel",e)