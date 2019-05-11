from django.core.management.base import BaseCommand , CommandError
from simplify.models import simpleURL
class Command(BaseCommand):
    help='Refreshes all existing shortcodes'
    def handle(self,*args,**options):
        return simpleURL.objects.refresh_code()
