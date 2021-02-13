"""Основной модуль домашнего задания темы Датаклассы."""
import re
from datetime import datetime, date
from my_child import Child, Parent
from my_ticket import TicketParent, TicketChild, TicketExcursion

ERROR_INPUT = "Ошибка ввода! Вы ввели не число. Попробуйте еще раз."


def calculate_age(birth_date):
    """Вычисление возраста посетителя для тестового набора данных."""
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        age -= 1
    return age


def check_age(func):
    """Определение вариантов посещения."""
    print("Возраст посетителя", func, end=" лет. ")
    if func < 4:
        print("Возможна только экскурсия по детскому центру в сопровождении взрослого.")
    elif 4 <= func < 7:
        print("Посещение возможно либо в сопровождении взрослого, либо в сопровождении старшего ребенка.")
    elif func >= 7:
        print("Возможно самостоятельное посещение.")
    return


def word_check(word):
    """Введенные данные должны состоять только из букв русского алфавита."""
    if re.search(r'[^а-яА-ЯёЁ]', word):
        raise ValueError("Ошибка ввода! Буквы должны быть только русского алфавита.")


def number_check(number):
    """Номер телефона должен начинаться с префикса "+7" или цифры 8 и иметь длину 10 цифр."""
    if re.search(r'(\+7|8)(\d{10})', number) and len(number) == 10:
        raise ValueError("Ошибка ввода! Номер должен быть длиной 10 знаков и начинаться с 8 или 9.")


def date_check(date):
    """Проверка правильности ввода даты."""
    try:
        return datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Ошибка ввода! Введите дату корректно.")


def create_child_instance():
    """Создание экземпляра класса Child."""
    print("Введите данные старшего ребенка.")
    first_name = input('Введите имя: ')
    word_check(first_name)
    last_name = input('Введите фамилию: ')
    word_check(last_name)
    date_entry = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    date_check(date_entry)
    year, month, day = map(int, date_entry.split('-'))
    birth_date = date(year, month, day)
    try:
        gen = int(input('Выберите пол (1 - мужской, 2 - женский): '))
    except ValueError:
        print(ERROR_INPUT)
    gender = ""
    if gen == 1:
        gender = 'муж'
    elif gen == 2:
        gender = 'жен'
    elif (gen != 1) and (gen != 2):
        raise ValueError("Ошибка ввода! Введите 1 или 2.")
    child = Child(first_name, last_name, birth_date, gender)
    return child


def create_parent_instance():
    """Создание экземпляра класса Parent."""
    print("Введите данные взрослого.")
    first_name = input('Введите имя: ')
    word_check(first_name)
    last_name = input('Введите фамилию: ')
    word_check(last_name)
    date_entry = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    date_check(date_entry)
    year, month, day = map(int, date_entry.split('-'))
    birth_date = date(year, month, day)
    gen = int(input('Выберите пол (1 - мужской, 2 - женский): '))
    gender = ""
    if gen == 1:
        gender = 'муж'
    elif gen == 2:
        gender = 'жен'
    elif (gen != 1) and (gen != 2):
        raise ValueError("Ошибка ввода! Введите 1 или 2")
    phone = input('Введите номер телефона: ')
    number_check(phone)
    cat = int(input('Вы имеете льготы? Если да, укажите их (1 - инвалид, 2 - многодетный, 3 - нет): '))
    if (cat != 1) and (cat != 2) and (cat != 3):
        raise ValueError("Ошибка ввода! Введите 1, 2 или 3")
    else:
        if cat == 1:
            category = "инвалид"
        elif cat == 2:
            category = "многодетный"
        elif cat == 3:
            category = ""
    parent = Parent(first_name, last_name, birth_date, gender, phone, category)
    return parent


def calculate_age_manual(birth_date):
    """Определение возраста посетителя."""
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


if __name__ == '__main__':
    print("\nДобро пожаловать в детский центр!")
    try:
        menu = int(input('Выберите способ навигации (1 - ручной ввод, 2 - тестовый набор): '))
    except ValueError:
        print(ERROR_INPUT)
    else:
        if menu == 1:
            i = 1
            j = 0
            companion = 0
            print('У нас возможна следующая продолжительность посещения: 1 час, 2 часа, 3 часа (безлимит).\n')
            try:
                duration = int(input('Выберите продолжительность посещения (1, 2 или 3): '))
            except ValueError:
                print(ERROR_INPUT)
            else:
                if (duration != 1) and (duration != 2) and (duration != 3):
                    raise ValueError("Ошибка ввода! Введите 1, 2 или 3")
                else:
                    while j != 1:
                        try:
                            pos = int(input('Выберите категорию посетителя (1 - ребенок, 2 - взрослый): '))
                        except ValueError:
                            print(ERROR_INPUT)
                        else:
                            if pos == 1:
                                child_i = create_child_instance()
                                #Проверяем возможность посещения в соответствии с возрастом ребенка
                                if calculate_age_manual(child_i.birth_date) >= 7:
                                    print("Возможно самостоятельное посещение.")
                                    ticket_child_i = TicketChild(i, datetime.now(), duration, child_i.first_name, child_i.last_name)
                                    print(ticket_child_i.get_description())
                                    #companion нужен для сопровождения младшего ребенка старшим
                                    companion = 1
                                elif 4 <= calculate_age_manual(child_i.birth_date) < 7:
                                    #взрослый не нужен, если companion уже присуствует
                                    if companion == 1:
                                        print("Возможно посещение в сопровождении старшего ребенка.")
                                        ticket_child_i = TicketChild(i, datetime.now(), duration, child_i.first_name, child_i.last_name)
                                        print(ticket_child_i.get_description())
                                    else:
                                        print("Возможно только посещение в сопровождении взрослого.")
                                        #оформляем экскурсионный билет только для взрослого
                                        parent_i = create_parent_instance()
                                        tick_parent_i = TicketParent(i, datetime.now(), duration, parent_i.first_name, parent_i.last_name, parent_i.category)
                                        print(tick_parent_i.get_description())
                                        if parent_i.category != "":
                                            #доработать функционал категорий посетителей
                                            print('Вам положена скидка!')
                                else:
                                    print("Возможна только экскурсия по детскому центру продолжительностью 1 час и в сопровождении взрослого.")
                                    duration = 1
                                    parent_i = create_parent_instance()
                                    ticket_exc_child_i = TicketExcursion(i, datetime.now(), child_i.first_name, child_i.last_name)
                                    ticket_exc_parent_i = TicketExcursion(i, datetime.now(), child_i.first_name, child_i.last_name)
                                    print(ticket_exc_child_i.get_description())
                                    print(ticket_exc_parent_i.get_description())
                            elif pos == 2:
                                if i == 1:
                                    parent_i = create_parent_instance()
                                    tick_parent_i = TicketParent(i, datetime.now(), duration, parent_i.first_name,
                                    parent_i.last_name, parent_i.category)
                                    print(tick_parent_i.get_description())
                                    print("Держите билеты. Проходите на экскурсию.")
                                else:
                                    parent_i = create_parent_instance()
                                    tick_parent_i = TicketParent(1, datetime.now(), duration, parent_i.first_name, parent_i.last_name,
                                                                 parent_i.category)
                                    print(tick_parent_i.get_description())
                            else:
                                raise ValueError("Ошибка ввода! Введите 1 или 2")
                            add = int(input('Добавить еще посетителя? \n 1 - Да, 2 - Нет\n'))
                            #доработать функционал добавления еще одного посетителя в случае если посещение экскурсионное.
                            if add == 1:
                                i = i + 1
                            if add == 2:
                                print("Держите билеты. Надеемся что вам все понравится.")
                                j = 1
        elif menu == 2:
            child_0 = Child("Иван", "Иванов", "2014-08-04", "муж")
            child_0.greeting()
            print(child_0.get_description())
            child_0.read_visit()
            calculate_age(child_0.birth_date)
            #Проверяем возможность посещения в соответствии с возрастом ребенка
            check_age(calculate_age(child_0.birth_date))
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
        else:
            raise ValueError("Ошибка ввода! Введите 1 или 2")
    finally:
        print("Выполнение программы завершено.")