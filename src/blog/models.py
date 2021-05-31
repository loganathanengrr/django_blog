import os
import random

from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

User = settings.AUTH_USER_MODEL

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1,3910209312)
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f"images/{final_filename}"

class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now)

class BlogPostManager(models.Manager):
	def get_queryset(self):
		return BlogPostQuerySet(self.model, using=self._db)

	def published(self):
		return self.get_queryset().published()


class BlogPost(models.Model):
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image   = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    title   = models.CharField(max_length=255)
    slug    = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
    	ordering = ['-publish_date', '-updated', '-created']

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
    	return f"/blog/{self.slug}/"

    def get_edit_url(self):
    	return f"{self.get_absolute_url()}edit/"

    def get_delete_url(self):
    	return f"{self.get_absolute_url()}delete/"
