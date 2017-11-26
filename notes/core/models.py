from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=140, blank=True)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'

