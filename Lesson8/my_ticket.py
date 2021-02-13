"""В этом модуле описаны классы, связанные с созданием билетов"""
from my_child import Child, Parent


class Ticket():
    """Родительский класс с атрибутами номер и дата."""
    def __init__(self, number, time_stamp):
        self.number = number
        self.time_stamp = time_stamp


class TicketParent(Ticket, Parent):
    """Здесь предполагалось использовать множественное наследование от 2х классов: Ticket и Parent.
    Но тогда надо использовать все атрибуты каждого из классов. А от класса Parent атрибуты birth_date, gender, phone в
    билете не нужны. Поэтому заново указал те атрибуты, которые требуются."""
    def __init__(self, number, time_stamp, duration, first_name, last_name, category):
        super().__init__(number, time_stamp)
        self.duration = duration
        self.first_name = first_name
        self.last_name = last_name
        self.category = category


    def get_description(self):
        """Высод информации о билете посетителя."""
        about_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration} ч., Посетитель {self.first_name} {self.last_name} Льгота: {self.category}"
        return about_ticket.title()


class TicketChild(Ticket, Child):
    """Так же как и в классе TicketParent, здесь предполагалось использовать множественное наследование от 2х классов: Ticket и Parent."""
    def __init__(self, number, time_stamp, duration, first_name, last_name):
        super().__init__(number, time_stamp)
        self.duration = duration
        self.first_name = first_name
        self.last_name = last_name


    def get_description(self):
        """Высод информации о билете посетителя."""
        about_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration} ч., Посетитель {self.first_name} {self.last_name}"
        return about_ticket.title()


class TicketExcursion(Ticket):
    """Класс для экскурсионного билета."""
    def __init__(self, number, time_stamp, first_name, last_name, note="экскурсия"):
        super().__init__(number, time_stamp)
        self.first_name = first_name
        self.last_name = last_name
        self.note = note


    def get_description(self):
        """Вывод информации об экскурсионном билете."""
        about_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Посетитель {self.first_name} {self.last_name}, Примечание: {self.note}"
        return about_ticket.title()