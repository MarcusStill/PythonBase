from django.test import TestCase
from .models import Visitor, Ticket, Visit


# Create your tests here.
class TestVisitor(TestCase):

    def setUp(self):
        self.visitor = Visitor.objects.create(first_name='Петр', last_name='Петросян', birthdate='2000-01-01', gender='муж')
        print('setUp выполнен')


    def tearDown(self):
        print('tearDown выполнен')


    def test_first_name_max_length(self):
        max_length = self.visitor._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 20)


class TestTicket(TestCase):

    def setUp(self):
        self.visitor = Visitor.objects.create(first_name='Петр', last_name='Петросян', birthdate='2000-01-01', gender='муж')
        print('setUp выполнен')


    def test_ticket(self):
        self.ticket = Ticket.objects.create(name_visitors=self.visitor)
        self.assertEqual(self.ticket.get_number_of_ticket(), 1)


class TestVisit(TestCase):


    def setUp(self):
        self.visitor = Visitor.objects.create(first_name='Петр', last_name='Петросян', birthdate='2000-01-01', gender='муж')
        print('setUp выполнен')


    def test_visit(self):
        self.ticket = Ticket.objects.create(name_visitors=self.visitor)
        self.visit = Visit.objects.create(number_ticket=self.ticket, duration='три')

    def test_visit_many(self):
        self.ticket = Ticket.objects.create(name_visitors=self.visitor)
        self.visit = Visit.objects.create(number_ticket=self.ticket, duration='1')
        self.ticket = Ticket.objects.create(name_visitors=self.visitor)
        self.visit = Visit.objects.create(number_ticket=self.ticket, duration='2')
        self.ticket = Ticket.objects.create(name_visitors=self.visitor)
        self.visit = Visit.objects.create(number_ticket=self.ticket, duration='3')
        self.assertEqual(self.visit.get_number_of_visit(), 3)