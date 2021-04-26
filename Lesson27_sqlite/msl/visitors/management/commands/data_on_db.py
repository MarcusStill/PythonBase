from django.core.management.base import BaseCommand
from visitors.models import Visit, Visitor, Ticket


class Command(BaseCommand):

    def handle(self, *args, **options):
        # del
        Visitor.objects.all().delete()
        Ticket.objects.all().delete()
        Visit.objects.all().delete()
