class Child():

    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.visit = 0


    def get_description(self):
        full_name = f"Информация о ребенке: {self.first_name} {self.last_name}, дата рождения: {self.birth_date}, пол: {self.gender}"
        return full_name.title()


    def greeting(self):
        print(f"Меня зовут {self.first_name} {self.last_name}.")


    def read_visit(self):
        print(f"Этот ребенок был в детском центре {self.visit} раз.")


    def update_visit(self, number):
        self.visit = number


class Parent(Child):

    def __init__(self, first_name, last_name, birth_date, gender, phone, category):
        super().__init__(first_name, last_name, birth_date, gender)
        self.phone = phone
        self.category = category


    def get_description(self):
        full_name = f"Информация о взрослом: {self.first_name} {self.last_name} {self.birth_date} {self.gender} №_тел {self.phone} категория {self.category}"
        return full_name.title()


    def update_visit(self):
        print("Количество посещений детского центра родителями не ведется!")