from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
COLOR_CHOICES = (
    ('default', 'Default'),
    ('blue', 'Blue'),
    ('red', 'Red'),
    ('yellow', 'Yellow'),
)

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=140, blank=True)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now) 
    color = models.CharField(max_length=120, default='default', choices=COLOR_CHOICES)

    def __str__(self):
        return f'{self.title}'

