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

    def calculate_age(birth_date):
        today = date.today()
        return today.year - child_i.birth_date.year - ((today.month, today.day) < (child_i.birth_date.month, child_i.birth_date.day))

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


class Ticket():

    def __init__(self, number, time_stamp, duration):
        self.number = number
        self.time_stamp = time_stamp
        self.duration = duration

    def get_description(self):
        about_ticket = f"Билет №{self.number}, {self.time_stamp}, продолжительность {self.duration} ч."
        return about_ticket.title()


class TicketParent(Ticket, Parent):

    def __init__(self, number, time_stamp, duration, first_name, last_name, category):
        super().__init__(number, time_stamp, duration)
        self.first_name = first_name
        self.last_name = last_name
        self.category = category

    def get_description(self):
        about_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration} ч., Посетитель {self.first_name} {self.last_name} Льгота {self.category}"
        return about_ticket.title()


class TicketChild(Ticket, Parent):

    def __init__(self, number, time_stamp, duration, first_name, last_name):
        super().__init__(number, time_stamp, duration)
        self.first_name = first_name
        self.last_name = last_name

    def get_description(self):
        about_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration} ч., Посетитель {self.first_name} {self.last_name}"
        return about_ticket.title()

class TicketExcursion(Ticket, Parent):
    pass

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        age -= 1
    #return print("Возраст: ", age)
    return age
''' Функция для тестового набора данных'''

def check_age(func):
    print("Возраст посетителя", func, end=" лет. ")
    if func <= 4:
        print("Возможна только экскурсия по детскому центру в сопровождении родителей.")
    elif func >= 5:
        print("Возможно только посещение в сопровождении родителей.")
    elif func > 8:
        print("Возможно самостоятельное посещение.")
    return

def create_child_instance():
    print("Введите данные старшего ребенка.")
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    date_entry = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    year, month, day = map(int, date_entry.split('-'))
    birth_date = date(year, month, day)
    gen = input('Выберите пол (1 - мужской, 2 - женский): ')
    gender = ""
    if gen == 1:
        gender = 'муж'
    if gen == 2:
        gender = 'жен'
    child = Child(first_name, last_name, birth_date, gender)
    return child

def create_parent_instance():
    print("Введите данные взрослого.")
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    birth_date = datetime.strptime(input('Введите дату в формате ГГГГ-ММ-ДД: '), "%Y-%m-%d")
    gen = input('Выберите пол (1 - мужской, 2 - женский): ')
    gender = ""
    if gen == 1:
        gender = 'муж'
    if gen == 2:
        gender = 'жен'
    phone = input('Введите номер телефона: ')

    ''' WAF?! '''
    cat = input('Вы имеете льготы? Если да, укажите их (1 - инвалид, 2 - многодетный): ')
    if cat == 1:
        category = "инвалид"
    elif cat == 2:
        category = "многодетный"
    else:
        category = ""
    parent = Parent(first_name, last_name, birth_date, gender, phone, category)
    return parent

print("\nДобро пожаловать в детский центр!")
menu = int(input('Выберите способ навигации (1 - ручной ввод, 2 - тестовый набор): '))
if menu == 1:
    i = 1
    j = 0
    companion = 0
    print('У нас возможна следующая родолжительность посещения: 1 час, 2 часа, 3 часа (безлимит).\n')
    duration = int(input('Выберите продолжительность посещения (1, 2 или 3): '))
    while j != 1:
        pos = int(input('Выберите категорию посетителя (1 - ребенок, 2 - взрослый): '))
        if pos == 1:
            child_i = create_child_instance()
            if child_i.calculate_age() >= 7:
                print("Возможно самостоятельное посещение.")
                ticket_child_i = TicketChild(i, datetime.now(), duration, child_i.first_name, child_i.last_name)
                print(ticket_child_i.get_description())
                companion = 1
            elif 4 <= child_i.calculate_age() < 7:
                if companion == 1:
                    print("Возможно посещение в сопровождении старшего ребенка.")
                    ticket_child_i = TicketChild(i, datetime.now(), duration, child_i.first_name, child_i.last_name)
                    print(ticket_child_i.get_description())
                else:
                    print("Возможно только посещение в сопровождении родителей.")
                    parent_i = create_parent_instance()
                    tick_parent_i = TicketParent(i, datetime.now(), duration, parent_i.first_name, parent_i.last_name, parent_i.category)
                    print(tick_parent_i.get_description())
                    if parent_i.category != "":
                        print('Вам положена скидка!')
            else:
                print("Возможна только экскурсия по детскому центру в сопровождении родителей.")
                TicketExcursion
        elif pos == 2:
            if i == 1:
                print("Вы на экскурсии")
                TicketExcursion
            else:
                parent_i = create_parent_instance()
                tick_parent_i = TicketParent(1, datetime.now(), duration, parent_i.first_name, parent_i.last_name,
                                             parent_i.category)
                print(tick_parent_i.get_description())
        add = int(input('Добавить еще посетителя? \n 1 - Да, 2 - Нет\n'))
        if add == 1:
            i = i + 1
        if add == 2:
            print("Держите билеты. Надеемся что вам все понравится.")
            j = 1
else:
    child_0 = Child("Иван", "Иванов", "2014-08-04", "муж")
    child_0.greeting()
    #child_0.calculate_age()
    print(child_0.get_description())
    child_0.read_visit()
    calculate_age(child_0.birth_date)
    check_age(calculate_age(child_0.birth_date))  # Проверка возможности посещения
    if (calculate_age(child_0.birth_date))>=4:
        ticket_child_1 = TicketChild(1, datetime.now(), 1, child_0.first_name, child_0.last_name)
        print(ticket_child_1.get_description())
    child_0.update_visit(1)
    child_0.read_visit()
    parent_1 = Parent("Дмитрий", "Иванов", "1980-1-13", "муж", "123654", "многодетный")
    parent_1.update_visit()
    print(parent_1.get_description())
    tick_parent_1 = TicketParent(1, datetime.now(), 1, parent_1.first_name, parent_1.last_name, parent_1.category)
    print(tick_parent_1.get_description())