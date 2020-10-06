from bicycle import Bicycle

class ElectricBicycle(Bicycle):
    def __init__(self, brand, model, category, wheels, motor, battery, mileage):
        super().__init__(brand, model, category, wheels)
        self.motor = motor
        self.battery = battery
        self.mileage = mileage

    def get_description(self):
        full_name = f"{self.brand} {self.model}, категория {self.category}, диаметр колеса {self.wheels},  мотор {self.motor} Вт., {self.battery} Вт, Запас хода {self.mileage} км."
        return full_name.title()

    def describe_battery(self):
        print(f"Этот велосипед имеет мотор можностью {self.motor} Вт.")
