from calendar import c
from django import forms
from django.forms import ModelForm
from .models import Fridge, Recipe


class FridgeForm2(ModelForm):
    class Meta:
        model = Fridge
        fields = ['staged_ingr', 'staged_amt']