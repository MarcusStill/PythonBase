from icecream import ic
from datetime import datetime, date

class Human():

    def __init__(self, gender):
        self.gender = gender


class Child(Human):

    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender

    def get_description(self):
        aboutchild = f"{self.first_name}, {self.last_name}, {self.birth_date}, {self.gender}"
        return aboutchild.title()

    def calculate_age(self):
        self.birth_date = datetime.strptime(self.birth_date, "%d/%m/%Y")
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or today.month == self.birth_date.month and today.day < self.birth_date.day:
            age -= 1
        return age


class Parent(Child):

    def __init__(self, first_name, last_name, birth_date, gender, phone, category):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.phone = phone
        self.category = category

    def get_description(self):
        aboutparent = f"{self.first_name}, {self.last_name}, {self.birth_date}, {self.gender}, №_тел {self.phone}, Категория {self.category}"
        return aboutparent.title()


class Ticket():

    def __init__(self, number, time_stamp, duration):
        self.number = number
        self.time_stamp = time_stamp
        self.duration = duration

    def get_description(self):
        aboutticket = f"{self.number}, {self.time_stamp}, {self.duration}"
        return aboutticket.title()

    def check_age(func):
        print('Ваш возраст', func, end='. ')
        if func <= 4:
            print('Только экскурсия')
        elif func <= 7:
            print('Посещение, но с родителями')
        elif func > 8:
            print('Можно самому')
        return


class Sale(Ticket, Parent):
    def __init__(self, number, date, first_name, last_name, sum, status):
        super().__init__(number, date)
        super().__init__(first_name, last_name)
        self.sum = sum
        self.status = status


child_1 = Child('Иван', 'Иванов', '4/8/2014', 'муж')
# print(child_1.get_description())
ic(child_1.get_description())
ic(child_1.calculate_age())
parent_1 = Parent('Дмитрий', 'Иванов', '4/12/1980', 'муж', '123654', '-')
ic(parent_1.get_description())
tick_1 = Ticket(1, datetime.now(), 2)
ic(tick_1.get_description())
