from icecream import ic
from datetime import datetime, date

#ic.configureOutput(includeContext=True)

class Child():

    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender

    def get_description(self):
        full_name = f"{self.first_name} {self.last_name} {self.birth_date}, {self.gender}"
        return full_name.title()

    ''' Если перенести функцию calculate_age внутрь класса Child, то к ней не получится обратиться следующим образом:
        age = child_1.calculate_age(child_1.birth_date)
        TypeError: calculate_age() takes 1 positional argument but 2 were given
    '''


class Parent(Child):

    def __init__(self, first_name, last_name, birth_date, gender, phone, category):
        super().__init__(first_name, last_name, birth_date, gender)
        self.phone = phone
        self.category = '-'

    def get_description(self):
        full_name = f"Посетитель: {self.first_name} {self.last_name} {self.birth_date} {self.gender}, №_тел {self.phone}, категория {self.category}"
        return full_name.title()


class Ticket():

    def __init__(self, number, time_stamp, duration):
        self.number = number
        self.time_stamp = time_stamp
        self.duration = duration


    def get_description(self):
        about_ticket = f"№{self.number}, {self.time_stamp}, продолжительность {self.duration}"
        return about_ticket.title()


class TicketParent(Ticket, Parent):

    def __init__(self, number, time_stamp, duration, first_name, last_name):
        super().__init__(number, time_stamp, duration)
        self.first_name = first_name
        self.last_name = last_name

    def get_description(self):
        print_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration}, Посетитель {self.first_name} {self.last_name}"
        return print_ticket.title()


class TicketChild(Ticket, Parent):

    def __init__(self, number, time_stamp, duration, first_name, last_name):
        super().__init__(number, time_stamp, duration)
        self.first_name = first_name
        self.last_name = last_name

    def get_description(self):
        print_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration}, Посетитель {self.first_name} {self.last_name}"
        return print_ticket.title()

# class Sale(Ticket, Parent):
#     def __init__(self, number, date, first_name, last_name, sum, status):
#         super().__init__(number, date)
#         super().__init__(first_name, last_name)
#         self.sum = sum
#         self.status = status

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        age -= 1
    return age

def check_age(func):
    print('Ваш возраст', func, end='. ')
    if func <= 4:
        print('Только экскурсия')
    elif func >= 5:
        print('Посещение, но с родителями')
    elif func > 8:
        print('Можно самому')
    return

child_1 = Child('Иван', 'Иванов', '2014-8-4', 'муж')
print(child_1.get_description())
parent_1 = Parent('Дмитрий', 'Иванов', '1980-1-13', 'муж', '123654', '')
print(parent_1.get_description())
tick_p = TicketParent(1, datetime.now(), 1, parent_1.first_name, parent_1.last_name)
print(tick_p.get_description())
print('Возраст ребенка ', calculate_age(child_1.birth_date), 'лет.')
check_age(calculate_age(child_1.birth_date))

#age = calculate_age(child_1.birth_date)
if (calculate_age(child_1.birth_date))>=4:
    tick_child = TicketChild(1, datetime.now(), 1, child_1.first_name, child_1.last_name)
print(tick_child.get_description())