from django.core.management.base import BaseCommand
from school.models import Teacher, Student

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Teacher.objects.all().delete()
        Student.objects.all().delete()




