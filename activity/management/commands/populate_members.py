from activity.factories import MemberFactory
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Write No. of entries'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of activity periods')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            mem=MemberFactory()
            mem.create()
            