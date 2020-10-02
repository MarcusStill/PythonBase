from bicycle import Bicycle

class ElectricBicycle(Bicycle):
    #def __init__(self, brand, model, wheels, year, motor, battery, mileage):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.motor = motor
        self.battery = battery
        self.mileage = mileage

    def get_description(self):
        full_name = f"{self.brand} {self.model} {self.year}, {motor} Вт., {battery} В, {mileage} км."
        return full_name.title()

    def describe_battery(self):
        print(f"Этот велосипед имеет мотор можностью {self.motor} Вт.")
