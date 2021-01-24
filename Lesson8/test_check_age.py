from datetime import datetime, date

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        age -= 1
    #return print("Возраст: ", age)
    return age

def check_age(func):
    print('Ваш возраст', func, end='. ')
    if func <= 4:
        print('Только экскурсия')
    elif func <= 7:
        print('Посещение, но с родителями')
    elif func > 8:
        print('Можно самому')
    return


res = check_age(calculate_age('4/8/2018'))
res1 = check_age(calculate_age('4/8/2014'))
res2 = check_age(calculate_age('4/8/2010'))