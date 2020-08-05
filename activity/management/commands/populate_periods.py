from activity.factories import PeriodFactory
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Write No. of entries'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of Members to be added')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            p=PeriodFactory()
            p.create()
            