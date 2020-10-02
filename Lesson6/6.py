print('Home work lesson 3')

from bicycle import Bicycle
from electric_bicycle import ElectricBicycle

bicycle_1 = Bicycle('GT', 'Aggressor', 'Mountain', '27', '2020')
print(bicycle_1.get_description())
#bicycle_1.update_odometr(5)
bicycle_1.read_odometr()
bicycle_el = ElectricBicycle('Ancher', 'Electric', '2020', '350', '36', '40')
print(bicycle_el.get_description())