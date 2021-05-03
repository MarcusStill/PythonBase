from django.contrib import admin
from .models import Visitor, Ticket, Visit

# Register your models here.
admin.site.register(Visitor)
admin.site.register(Visit)
admin.site.register(Ticket)