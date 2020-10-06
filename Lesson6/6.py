print('Home work lesson 3')

from bicycle import Bicycle
from electric_bicycle import ElectricBicycle

bicycle_1 = Bicycle('GT', 'Aggressor', 'Mountain', '27')
print(bicycle_1.get_description())
#bicycle_1.update_odometr(5)
bicycle_1.read_odometr()
bicycle_el = ElectricBicycle('Ancher', 'X-1', 'Electric', '26', '350', '123', '30')
print(bicycle_el.get_description())