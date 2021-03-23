thouth = int(input())
if thouth % 1000 == 0:
    print('millenium')
else:
    print('try it again')
#------------------------------
family = input()
age = 0
if family.isdigit():
    age = int(family)
    if age > 50:
        print('to order restaurant')
    elif age in range(20,50):
        print('to order caffe')
    elif age < 20:
        print('home, sweet home')

#-------------------------------------
init = input()
if len(init) > 10:
    init += '!'
    print(init)
else:
    print(init[2])

#------------------------------------
enter = input("enter a word: ")

fsrt = len(enter)
mid = fsrt / 2
if fsrt % 2 == 0:
    print(enter[int(mid) - 1:int(mid)])
elif enter[int(mid)] == enter[0]:
    print(enter[1:-1])
elif fsrt % 2 != 0:
    print(enter[int(mid)])