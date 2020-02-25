from django.shortcuts import render
from django.http import HttpRequest

from .models import Note

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, "pk": pk})