class Bicycle():

    def __init__(self, brand, model, category, wheels):
        self.brand = brand
        self.model = model
        self.category = category
        self.wheels = wheels
        self.odometr = 0


    def get_description(self):
        full_name = f"{self.brand} {self.model}, категория {self.category}, диаметр колеса {self.wheels}"
        return full_name.title()

    def read_odometr(self):
        print(f'Этот велосипед проехал {self.odometr} км.')

    def update_odometr(self, km):
        if km >= self.odometr:
            self.odometr = km
        else:
            print('Ошибка ввода данных!')

    def increment_odometr(self, km):
        if km <= 0:
            self.odometr +=km
        else:
            print('Ошибка ввода данных!')