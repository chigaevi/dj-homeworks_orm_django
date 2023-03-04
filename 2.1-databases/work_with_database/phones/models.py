from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, null=False, unique=True)
    price = models.CharField(max_length=20, null=False)
    image = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()

    def get_url(self):
        return reverse('phone', args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # взял тут - https://learndjango.com/tutorials/django-slug-tutorial
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
