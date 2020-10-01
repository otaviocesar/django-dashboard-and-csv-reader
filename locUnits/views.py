from django.shortcuts import render
from .models import LocUnit, Event
import pandas as pd
from .utils import get_simple_plot, get_salesman_from_id, get_image
from .forms import EventForm
from django.http import HttpResponse
import matplotlib.pyplot as plt 
import seaborn as sns 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_event_view(request):
    form = EventForm(request.POST or None)
    added_message=None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()

        form = EventForm()
        added_message = "The event has been added"

    context = {
        'form': form,
        'added_message': added_message,
    }
    return render(request, 'locUnits/add.html', context)

    