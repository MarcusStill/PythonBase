from icecream import ic
from datetime import datetime, date

#ic.configureOutput(includeContext=True)

class Child():

    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.visit = 0

    def get_description(self):
        full_name = f"Информация о ребенке: {self.first_name} {self.last_name} {self.birth_date} {self.gender}"
        return full_name.title()

    def greeting(self):
        print(f"Меня зовут {self.first_name} {self.last_name}.")

    def calculate_age(self):
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        today = date.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
            age -= 1
        print("Мне", age, "лет.")

    def read_visit(self):
        print(f"Этот ребенок был в детском центре {self.visit} раз.")

    def update_visit(self, number):
        self.visit = number


class Parent(Child):

    def __init__(self, first_name, last_name, birth_date, gender, phone, category):
        super().__init__(first_name, last_name, birth_date, gender)
        self.phone = phone
        self.category = "-"

    def get_description(self):
        full_name = f"Информация о взрослом: {self.first_name} {self.last_name} {self.birth_date} {self.gender} №_тел {self.phone} категория {self.category}"
        return full_name.title()

    def update_visit(self):
        print("Количество посещений детского центра родителями не ведется!")


class Ticket():

    def __init__(self, number, time_stamp, duration):
        self.number = number
        self.time_stamp = time_stamp
        self.duration = duration

    def get_description(self):
        about_ticket = f"Билет №{self.number}, {self.time_stamp}, продолжительность {self.duration}"
        return about_ticket.title()


class TicketParent(Ticket, Parent):

    def __init__(self, number, time_stamp, duration, first_name, last_name, category):
        super().__init__(number, time_stamp, duration)
        self.first_name = first_name
        self.last_name = last_name
        self.category = category

    def get_description(self):
        print_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration}, Посетитель {self.first_name} {self.last_name} Категория {self.category}"
        return print_ticket.title()


class TicketChild(Ticket, Parent):

    def __init__(self, number, time_stamp, duration, first_name, last_name):
        super().__init__(number, time_stamp, duration)
        self.first_name = first_name
        self.last_name = last_name

    def get_description(self):
        print_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration}, Посетитель {self.first_name} {self.last_name}"
        return print_ticket.title()


def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        age -= 1
    return age
''' Если перенести функцию calculate_age внутрь класса Child, то к ней не получится обратиться следующим образом:
    age = child_1.calculate_age(child_1.birth_date)
    TypeError: calculate_age() takes 1 positional argument but 2 were given'''

def check_age(func):
    print("Возраст посетителя", func, end=" лет. ")
    if func <= 4:
        print("Возможна только экскурсия по детскому центру в сопровождении родителей.")
    elif func >= 5:
        print("Возможно только посещение в сопровождении родителей.")
    elif func > 8:
        print("Возможно самостоятельное посещение.")
    return


child_1 = Child("Иван", "Иванов", "2014-8-4", "муж")
child_1.greeting()
child_1.calculate_age()
print(child_1.get_description())
child_1.read_visit()
check_age(calculate_age(child_1.birth_date)) #Проверка возможности посещения
if (calculate_age(child_1.birth_date))>=4:
    ticket_child_1 = TicketChild(1, datetime.now(), 1, child_1.first_name, child_1.last_name)
    print(ticket_child_1.get_description())
child_1.update_visit(1)
child_1.read_visit()
parent_1 = Parent("Дмитрий", "Иванов", "1980-1-13", "муж", "123654", "")
parent_1.update_visit()
print(parent_1.get_description())
tick_parent_1 = TicketParent(1, datetime.now(), 1, parent_1.first_name, parent_1.last_name, parent_1.category)
print(tick_parent_1.get_description())
#print("Возраст ребенка ", calculate_age(child_1.birth_date), "лет.") #Проверяем возраст


