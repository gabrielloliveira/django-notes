from django.contrib import admin
from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ['author__username', 'author__email', 'title']


admin.site.register(Note, NoteAdmin)