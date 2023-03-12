from django.core.management.base import BaseCommand
import json
from school.models import Teacher, Student

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('school.json', 'r') as file:
            schooldata = json.load(file)
        # print(schooldata)
        for data in schooldata:
            if data['model'] == 'school.teacher':
                Teacher.objects.create(
                    id=data['pk'],
                    name=data['fields']['name'],
                    subject=data['fields']['subject'],
                )
            elif data['model'] == 'school.student':
                Student.objects.create(
                    name=data['fields']['name'],
                    teachers=data['fields']['teachers'],
                    group=data['fields']['group'],
                )
