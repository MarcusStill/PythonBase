class Bicycle():

    def __init__(self, brand, model, category, wheels):
        self.brand = brand
        self.model = model
        self.category = category
        self.wheels = wheels

    def get_description(self):
        specification = f"{self.brand} {self.model}, категория {self.category}, диаметр колеса {self.wheels}"
        return specification.title()
