from django.core.management.base import BaseCommand
from articles.models import Article

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Article.objects.all().delete()

