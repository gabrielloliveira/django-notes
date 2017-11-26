from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    user = request.user
    notes_this_user = Note.objects.filter(author=user).order_by('-date_created')
    return render(request, 'site/home.html', {'notes': notes_this_user})


@login_required
def create_note(request):
    form = NoteForm
    
    if request.POST:
        data = {
          'author': request.user.id,
          'title': request.POST['title'],
          'content': request.POST['content']
        }
        new_note = NoteForm(data)
        if new_note.is_valid():
            new_note.save(data)

        return HttpResponseRedirect("/home/")

    return render(request, 'site/create-note.html', {'form': form})
    