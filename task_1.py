import random
number = input("Введите загаданное вами число: \n")
x = int(input('начало промежутка:\n'))
y = int(input('конец промежутка:\n'))
tries = int(input('колличество попыток:\n'))
computer_number = random.randrange(x, y+1)
while x != y:
    print("Ваше число равно,больше или меньше:\n", computer_number)
    z = input()
    if 'больше' in z.lower():
            x = computer_number
            computer_number = random.randrange(x, y)
            tries -= 1
    elif 'меньше' in z.lower():
            y = computer_number
            computer_number = random.randrange(x, y)
            tries -= 1
            if tries == 0:
                break

    elif 'равно' in z.lower():
            break
print('Ваше число:', number, ' ,а число найденное компьютером: ', computer_number, 'кол-во попыток:', tries)