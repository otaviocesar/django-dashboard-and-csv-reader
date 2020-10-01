from django import forms
from .models import LocUnit, Event

class EventForm(forms.ModelForm):
    locUnit = forms.ModelChoiceField(queryset=LocUnit.objects.all(),
                                    label='LocUnit',
                                    widget=forms.Select(attrs={'class': 'ui selection dropdown field-with'}))
    class Meta:
        model = Event
        fields = ['locUnit']