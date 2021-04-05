listin = [15, 56, 64, 561, 9, 94, 12, ]
z = list(map(lambda x: x * (-2), listin))
print(z)

listen2 = []
for x in listin:
    x *= (-2)
    listen2.append(x)

print(listen2)
#---------------------------------------

list = [15, 56, 64, 561, 9, 94, 12, ]
list2 = []
i = 0
while i < len(list):
    num = list[i]
    num *= (-2)
    i += 1
    list2.append(num)

print(list2)
#-------------------------------------------

ls = [1, 2, 3, 54, 55, 74, 45, 10]
count2 = 0
for i in ls:
    if i % 2 == 0:
        count2 += 1

print(count2)

#-----------------------------------


ls2 = [1, 2, 3, 54, 55, 74, 45, 10]
i = 0
count = 0
while i < len(ls2):
    num = ls2[i]
    i += 1
    if num % 2 == 0:
        count += 1

print(count)

#-----------------------------------


def uvi(**kwargs):
    dgdr = {key + str(len(key)):value for key,value in kwargs.items()}
    print(f'{dgdr}')


uvi(mai=45)

#------------------------------------------------

mai = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
while mai:
    for key in mai.keys():
        print(f'{key}{str(len(key))}')
    break
#------------------------------------------------
lis = [1, 2, 3, 4, 5, 6 ]
x = lis[1:]+lis[:1]

print(x)
#--------------------------


a = [1, 2, 3, 4, 5, 6]
b = []
while a:
    x = a[1:] + [0]
    b.extend(x)
    break
print(b)

