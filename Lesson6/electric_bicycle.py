from bicycle import Bicycle

class Battery():

    def __init__(self, battery_size=7):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Этот велосипед имеет аккумулятор емкостью {self.battery_size} Ah.")

    def get_range(self):
        if self.battery_size == 7:
            range = 25
        elif self.battery_size == 10:
            range = 40
        print(f"Этот велосипед проедет примерно {range} km на полном заряде аккумулятора.")


class ElectricBicycle(Bicycle):

    def __init__(self, brand, model, category, wheels, motor, mileage):
        Bicycle.__init__(self, brand, model, category, wheels)
        self.motor = motor
        self.mileage = 0
        self.odometr = 0
        self.battery = Battery()

    def get_description(self):
        specification = f"{self.brand} {self.model}, категория {self.category}, диаметр колеса {self.wheels},  мотор {self.motor} Вт, Запас хода {self.mileage} км."
        return specification.title()

    def read_odometr(self):
        print(f'Этот велосипед проехал {self.odometr} км.')

    def drive(self, km):
        if self.mileage >= km:
            self.odometr += km
            self.mileage -= km
        else:
            print('Батарея разряжена. Зарядите аккумулятор!')

    def charge_battery(self):
        if self.battery.battery_size == 7:
            self.mileage=25
            print('Батарея заряжена!')
        elif self.battery.battery_size == 10:
            self.mileage=40
            print('Батарея заряжена!')

    def battery_info(self):
        print(f'Запас хода {self.mileage} км.')
