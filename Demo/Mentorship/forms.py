from django.forms import ModelForm
from .models import Users
from django import forms

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'