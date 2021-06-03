from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL


class SearchQuery(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	query = models.CharField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True)
