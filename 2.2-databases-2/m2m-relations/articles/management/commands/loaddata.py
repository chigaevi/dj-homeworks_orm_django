from django.core.management.base import BaseCommand
import json
from articles.models import Article

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('articles.json', 'r') as file:
            articles_data = json.load(file)
            print(articles_data)
        for data in articles_data:
            Article.objects.create(
                pk=data['pk'],
                title=data['fields']['title'],
                text=data['fields']['text'],
                published_at=data['fields']['published_at'],
                image=data['fields']['image'],
            )

