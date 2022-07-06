from cProfile import label
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelChoiceField, ModelForm,EmailField
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class AddTerm(ModelForm):
    date_start = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    date_end = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Term
        fields = ['academicyear','date_start','date_end']

        labels={
            'academicyear':'Academic Year',
            'date_start':'Starting Date',
            'date_end':'End Date',
        }
class AddCollege(ModelForm):
    class Meta:
        model = College
        fields = ['name']

class AddBuild(ModelForm):
    class Meta:
        model = Building
        fields = ['name','college']

class AddDept(ModelForm):
    class Meta:
        model = Department
        fields = ['name','college']

class AddRoom(ModelForm):
    class Meta:
        model = Room
        fields = ['name','college','building','capacity']
