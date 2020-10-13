from bicycle import Bicycle
from exeptions import MyError

class Battery():

    def __init__(self, battery_size=7):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Этот велосипед имеет аккумулятор емкостью {self.battery_size} Ah.\n")

    def get_range(self):
        if self.battery_size == 7:
            range = 25
        elif self.battery_size == 10:
            range = 40
        print(f"Этот велосипед проедет примерно {range} km на полном заряде аккумулятора.\n")


class ElectricBicycle(Bicycle):

    def __init__(self, brand, model, category, wheels, motor, mileage):
        Bicycle.__init__(self, brand, model, category, wheels)
        self.motor = motor
        self.mileage = 0
        self.odometr = 0
        self.battery = Battery()

    def __str__(self):
        return f'Велосипед {self.brand} {self.model}, категория {self.category}, диаметр колеса {self.wheels},  мотор {self.motor} Вт, емкость аккумулятора {self.mileage} Ah.\n'

    def read_odometr(self):
        print(f'Велосипед {self.brand} {self.model} проехал {self.odometr} км.\n')

    def drive(self, km):
        if self.mileage >= km:
            self.odometr += km
            self.mileage -= km
        else:
            print(f'Батарея велосипеда {self.brand} {self.model} разряжена. Зарядите аккумулятор!\n')

    def charge_battery(self):
        if self.battery.battery_size == 7:
            self.mileage=25
            print(f'Батарея велосипеда {self.brand} {self.model} заряжена!\n')
        elif self.battery.battery_size == 10:
            self.mileage=40
            print(f'Батарея велосипеда {self.brand} {self.model} заряжена!\n')

    def battery_info(self):
        print(f'Запас хода велосипеда {self.brand} {self.model} составляет {self.mileage} км.\n')