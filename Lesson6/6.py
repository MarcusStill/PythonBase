print('Home work lesson 3')

class Bicycle():

    def __init__(self, brand, model, category, wheels, year):
        self.brand = brand
        self.model = model
        self.category = category
        self.wheels = wheels
        self.year = year
        self.odometr = 0


    def get_description(self):
        full_name = f"{self.brand} {self.model} {self.category} {self.wheels}"
        return full_name.title()

    def read_odometr(self):
        print(f'This bicycle has {self.odometr} km on it.')

    def update_odometr(self, km):
        self.odometr = km

bicycle_1 = Bicycle('GT', 'Aggressor', 'mountain', '27', '2019')
print(bicycle_1.get_description())
bicycle_1.update_odometr(5)
bicycle_1.read_odometr()

