print('Home work lession 3')

class Transport():
    def __init__(self, name, type, weight, loading_capacity):
        self.name = name
        self.type = type
        self.weight = weight
        self.loadinh_capaciry = loading_capacity

    def make_a_sound(self):
        print(f"{self.name} make a sound 'bi-bi'")

car = Transport('Skoda', 'passenger', '1100 kg', '500 kg')
car.make_a_sound()

plane = Transport('AN-22', 'cargo', '118000 kg', '80000 kg')
ship = Transport('Titanik', 'passendger', '52000 t', '200000 kg')