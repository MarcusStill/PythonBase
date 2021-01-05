from datetime import datetime, date

class Child():

    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_description(self):
        aboutchild = f"Имя: {self.first_name}, фамилия: {self.last_name}, дата рождения: {self.birth_date}"
        return aboutchild.title()

    def calculate_age(self):
        self.birth_date = datetime.strptime(self.birth_date, "%d/%m/%Y")
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or today.month == self.birth_date.month and today.day < self.birth_date.day:
            age -= 1
        return print("Возраст: ", age)


class Adult(Child):

    def __init__(self, first_name, last_name, birth_date, phone, category):
        Child.__init__(first_name, last_name, birth_date)
        self.phone = phone
        self.category = category

    def get_description(self):
        aboutadult = f"Имя {self.first_name}, фамилия {self.last_name}, дата рождения {self.birth_date}, №_телефона {self.phone}, категория {self.category}"
        return aboutadult.title()


class Group(Adult, Child):
    def __int__(self):
        Adult.__init__()
        Child.__init__()

    pass

class Visitors():
    pass

child_1 = Child('Иван', 'Иванов', '4/8/2014')
print(child_1.get_description())
child_1.calculate_age()
