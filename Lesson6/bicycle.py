from exeptions import MyError

class Bicycle():

    def __init__(self, brand, model, category, wheels):
        self.brand = brand
        self.model = model
        self.category = category
        if wheels <= 1:
            raise MyError(wheels)
        self.wheels = wheels

    def __str__(self):
        return f'{self.brand} {self.model}, категория {self.category}, диаметр колеса {self.wheels} дюймов.\n'