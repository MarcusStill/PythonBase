from django.db import models
from datetime import date

# Create your models here.
class Visitor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateField(("Date"), default=date.today)
    gender = models.CharField(max_length=3)

    def __srt__(self):
        return self.last_name