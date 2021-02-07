# from datetime import datetime, date
#
# def calculate_age(birth_date):
#     #birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
#     birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
#     today = date.today()
#     age = today.year - birth_date.year
#     if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
#         age -= 1
#     #return print("Возраст: ", age)
#     return age
#
# def check_age(func):
#     print('Ваш возраст', func, end='. ')
#     if func <= 4:
#         print('Только экскурсия')
#     elif func <= 7:
#         print('Посещение, но с родителями')
#     elif func > 8:
#         print('Можно самому')
#     return
# class Child():
#
#     def __init__(self, first_name, last_name, birth_date, gender):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_date = birth_date
#         self.gender = gender
#         self.visit = 0
#
# res = check_age(calculate_age('2018-8-4'))
# res1 = check_age(calculate_age('2016-8-4'))
# res2 = check_age(calculate_age('2010-8-4'))
#
# posetitel = int(input('Введите количество посетителей: '))
# i = 1
# while posetitel >= i:
#     option = int(input('Выберите категорию посетителя: \n 1 - ребенок, 2 - взрослый\n'))
#     if option == 1:
#         nameVar = input('Type the name: ')
#         salVar = input('Type the salary: ')
#         dobVar = input('Type the doB: ')
#         titleVar = input('Type the title: ')
#
#         # Create the instance of the myStruct object
#         myInstance = myStruct(nameVar, salVar, dobVar, titleVar)
#
#     if option == 2:

''''''
# from datetime import datetime, date
# # date_entry = input('Enter a date in YYYY-DD format: \n')
# # year, month, day = map(int, date_entry.split('-'))
# # date1 = datetime.date(year, month, day)
# def calculate_age(birth_date):
#     birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
#     today = date.today()
#     age = today.year - birth_date.year
#     if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
#         age -= 1
#     return age
#
# #s = datetime.strptime(input('Enter a date in YYYY-DD format: '), "%Y-%m-%d")
# s = '2018-04-29'
# print(s)
# print(calculate_age(s))

# from datetime import datetime
#
# i = str(input('date: '))
# try:
#     dt_start = datetime.strptime(i, '%Y-%m-%d')
#     print(dt_start)
# except ValueError:
#     print("Incorrect format")
'''
'''
# from datetime import datetime, date
#
# # d = '2020-06-01'
# # date_in_datetime = datetime.strptime(d, '%Y-%m-%d').date()
# #
# # print(date_in_datetime)
#
# # dt_start = str(input('date: '))
# # dt_start = datetime.strptime(dt_start, '%Y-%m-%d')
# # print(dt_start)
#
#
# date_entry = input('Enter a date (i.e. 2017-7-1)')
# year, month, day = map(int, date_entry.split('-'))
# date = date(year, month, day)
# print(date)
# def calculate_age(birth_date):
#     birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
#     today = date.today()
#     age = today.year - birth_date.year
#     if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
#         age -= 1
#     return age
# print(calculate_age(date))
# from datetime import datetime
# from dataclasses import dataclass
#
#
# @dataclass
# class Human:
#     first_name: str
#     last_name: str
#     patronymic: str
#     date: datetime
#
#     def __post_init__(self):
#         self.date = datetime.strptime(self.date, '%d-%m-%Y')
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name + ' ' + self.patronymic + ' ' \
#                + datetime.strftime(self.date, '%d-%m-%Y')
#
#     @property
#     def age(self):
#         """Метод вычисления возраста по дате рождения"""
#         return (datetime.now() - self.date).days / 365.25
#
#
# humanOne = Human('Billy', 'Gibson', 'Hill', '20-02-1999')
# humanTwo = Human('Stella', 'MacCol', 'Denny', '30-12-1995')
# humanThree = Human('Kortney', 'MacCol', 'Denny', '15-09-1998')
#
# print(humanOne)
# print(humanOne.age)
# print(humanTwo)
# print(humanTwo.age)
# print(humanThree)
# print(humanThree.age)
from datetime import date


# def calculate_age(birth_date):
#     today = date.today()
#     age = today.year - birth_date.year
#     full_year_passed = (today.month, today.day) < (birth_date.month, birth_date.day)
#     if not full_year_passed:
#         age -= 1
#     return age
# ''''''
# from datetime import datetime, date
#
# def calculate_age(born):
#     today = date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
#
# date_entry = input('Enter a date (i.e. 2017-7-1)')
# year, month, day = map(int, date_entry.split('-'))
# date = date(year, month, day)
# print(date)
# print(type(date))
# print(calculate_age(date))