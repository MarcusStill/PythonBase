from django.db import models
from datetime import date

# Create your models here.
class Visitor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateField(("Date"), default=date.today)
    gender = models.CharField(max_length=3)

    class Meta:
        unique_together = ("first_name", "last_name")

    def __str__(self):
        return self.last_name


class Ticket(models.Model):
    number = models.AutoField
    name_visitors = models.ForeignKey(Visitor, on_delete=models.CASCADE)


    def get_number_of_ticket(self):
        num = Ticket.objects.filter().count()
        return num


class Visit(models.Model):
    visit_date = models.DateField(default=date.today)
    number_ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    duration = models.IntegerField()


    def get_number_of_visit(self):
        num = Visit.objects.filter().count()
        return num