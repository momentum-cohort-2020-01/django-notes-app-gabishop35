from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest

from .models import Note
from .forms import NoteForm
# from .forms import


# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_details.html', {'note': note, "pk": pk})

def notes_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        # note = form.save()
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            # note.published_date = timezone.now()
            note.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'core/notes_new.html', {'form': form})

def notes_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance = note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/notes_edit.html', {'form': form})

def notes_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes-list')
