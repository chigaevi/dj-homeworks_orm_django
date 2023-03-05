import json

from django.core.management.base import BaseCommand
from books.models import Book



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Book.objects.all().delete()
        print('db cleared successfully')

