from django.shortcuts import render
from django.http import HttpRequest

import data

# Create your views here.
def index(request):
    notes = data.NOTES
    # breakpoint()
    return render(request, 'base.html', {'notes': notes})