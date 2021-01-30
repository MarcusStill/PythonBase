from icecream import ic
from datetime import datetime, date

class Child():

    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender

    def get_description(self):
        full_name = f"{self.first_name} {self.last_name} {self.birth_date}, {self.gender}"
        return full_name.title()

    def calculate_age(self):
        self.birth_date = datetime.strptime(self.birth_date, "%d/%m/%Y")
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or today.month == self.birth_date.month and today.day < self.birth_date.day:
            age -= 1
        return age

class Parent(Child):

    def __init__(self, first_name, last_name, birth_date, gender, phone, category):
        super().__init__(first_name, last_name, birth_date, gender)
        self.phone = phone
        self.category = category

    def get_description(self):
        full_name = f"{self.first_name} {self.last_name} {self.birth_date} {self.gender}, №_тел {self.phone}, категория {self.category}"
        return full_name.title()


class Ticket():

    def __init__(self, number, time_stamp, duration):
        self.number = number
        self.time_stamp = time_stamp
        self.duration = duration


    def get_description(self):
        about_ticket = f"№{self.number}, {self.time_stamp}, продолжительность {self.duration}"
        return about_ticket.title()

    def check_age(func):
        print('Ваш возраст', func, end='. ')
        if func <= 4:
            print('Только экскурсия')
        elif func <= 7:
            print('Посещение, но с родителями')
        elif func > 8:
            print('Можно самому')
        return

# class TicketParent(Ticket, Parent):
#
#     def __init__(self, number, time_stamp, duration, first_name, last_name):
#         super().__init__(number, time_stamp, duration)
#         super().__init__(first_name, last_name)

class TicketParent(Parent):

    def __init__(self, number, time_stamp, duration, first_name, last_name):
        self.number = number
        self.time_stamp = time_stamp
        self.duration = duration
        self.first_name = first_name
        self.last_name = last_name

    def get_description(self):
        print_ticket = f"Билет № {self.number}, Дата {self.time_stamp}, Продолжительность {self.duration}, Посетитель {self.first_name} {self.last_name}"
        return print_ticket.title()

class TicketChild(Ticket, Child):

    def __init__(self, number, time_stamp, duration, first_name, last_name):
        super().__init__(self, number, time_stamp, duration)
        super().__init__(self, first_name, last_name)

# class Sale(Ticket, Parent):
#     def __init__(self, number, date, first_name, last_name, sum, status):
#         super().__init__(number, date)
#         super().__init__(first_name, last_name)
#         self.sum = sum
#         self.status = status


child_1 = Child('Иван', 'Иванов', '4/8/2014', 'муж')
# print(child_1.get_description())
ic(child_1.get_description())
ic(child_1.calculate_age())
parent_1 = Parent('Дмитрий', 'Иванов', '4/12/1980', 'муж', '123654', '-')
ic(parent_1.get_description())
#tick_1 = Ticket(1, datetime.now(), 2)
tick_p = TicketParent(1, datetime.now(), 1, parent_1.first_name, parent_1.last_name)
ic(tick_p.get_description())
#ic(tick_1.get_description())
