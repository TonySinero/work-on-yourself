class Man():

    def __init__(self, age, weight ,name):
        self.__age = age
        self.__name = name
        self.__weight = weight

    def set_name(self, new_name):
        if new_name == "Tom":
            return
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_age(self, new_age):
        self.__age = new_age

    def get_age(self):
        return self.__age

    def set_weight(self, new_weight):
        self.__weight = new_weight

    def get_weight(self):
        return self.__weight

    def printall(self):
        print(f'his name is {self.__name},age is {self.__age} and weight {self.__weight}')

def main():
    people = Man('23','75','Truma')
    people.printall()
    people.set_name('Liner')
    people.printall()
    people.set_age('25')
    people.set_weight('72')
    people.printall()
    people.get_age()


if __name__ == '__main__':
    main()



class Car():

    def __init__(self,marka, model, age, ):
        self.__marka = marka
        self.__model = model
        self.__age = age
        self.__speed = 0

    def set_marka(self,new_marka):
        self.__marka = new_marka

    def set_model(self,new_model):
        self.__model= new_model

    def set_age(self,new_age):
        self.__age = new_age

    def update_speed(self,new_speed):
        self.__speed = new_speed
        if new_speed > 200:
            self.__speed = 0

    def read_odometer(self):
        print("This car has " + str(self.__speed) + " speed")

    def increment_odometer(self, miles):
        self.__speed += miles



    def increment_odometer2(self, miles):
        self.__speed -= miles


    def get_descriptive_name(self):
        long_name = self.__marka + ' ' + self.__model + ' ' + str(self.__age)
        return print(long_name)

    def reverse_speed(self, miles):
        if self.__speed < 0:
            miles = -miles
        return print(miles)



def main():
   cars = Car('BMW','M5',2019)
   cars.get_descriptive_name()
   cars.update_speed(155)
   cars.read_odometer()
   cars.increment_odometer(5)
   cars.read_odometer()
   cars.increment_odometer2(10)
   cars.read_odometer()
   cars.reverse_speed(-12)

if __name__ == '__main__':
    main()