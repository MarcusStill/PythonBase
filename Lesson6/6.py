print('Home work lesson 6\n')

from exeptions import MyError
from bicycle import Bicycle
from electric_bicycle import ElectricBicycle

wheels_1 = int(input('Введите размер колеса велосипеда 1: '))
bicycle_1 = Bicycle('GT', 'Aggressor', 'Mountain', wheels_1)
try:
    bicycle_2 = Bicycle('Stern', 'Cross', 'Mountain', int('0'))
except:
    print('Ошибка ввода данных!')
print(bicycle_1)
bicycle_el = ElectricBicycle('Eltreco', 'INSIDER', 'Electric', int('20'), int('350'), int('10'))
print(bicycle_el)
bicycle_el.battery.describe_battery()
wheels_2 = int(input('Введите размер колеса велосипеда 2: '))
motor_2 = int(input('Введите мощность мотора велосипеда 2: '))
akb_2 = int(input('Введите емкость аккумулятора велосипеда 2: '))
bicycle_el2 = ElectricBicycle('Eltreco', 'DRIVER', 'Electric', wheels_2, motor_2, akb_2)
print(bicycle_el2)
bicycle_el.read_odometr()
bicycle_el.drive(10)
bicycle_el.charge_battery()
print(bicycle_el.battery_info())
bicycle_el.drive(5)
bicycle_el.read_odometr()
print(bicycle_el.battery_info())
bicycle_el.drive(25)
bicycle_el.charge_battery()
bicycle_el.drive(25)
bicycle_el.read_odometr()
