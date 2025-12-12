from blog.models import Post
from django.core.management.base import BaseCommand
from blog.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):
         
         categories = ["Food","Society","Nature"]
    
         for category in categories:
            Category.objects.create(category = category)
         self.stdout.write(self.style.SUCCESS('Completed inserting data'))