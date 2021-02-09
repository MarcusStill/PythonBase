from my_child import Parent


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
        about_ticket = f"Билет №{self.number}, Дата {self.time_stamp}, Продолжительность {self.duration} ч., Посетитель {self.first_name} {self.last_name} Льгота: {self.category}"
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