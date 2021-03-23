class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return print(self.x + self.y)

    def minus(self):
        return print(self.x - self.y)

    def multiply(self):
        return print(self.x * self.y)

    def devide(self):
        if self.y == 0:
            return print('wrong number!')
        return print(self.x / self.y)


def main():
    while True:
        s = input("Знак (+,-,*,/): ")
        if s == '0':
            break
        if s in ('+', '-', '*', '/'):
            x = float(input("x="))
            y = float(input("y="))
            ege = Math(x, y)
            if s == '+':
                ege.sum()
            elif s == '-':
                ege.minus()
            elif s == '*':
                ege.multiply()
            elif s == '/':
                ege.devide()
        else:
            print("Неверный знак операции!")

if __name__ == '__main__':
    main()