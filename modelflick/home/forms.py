from django import forms

from .models import services

class serviceform(forms.ModelForm):
    class Meta:
        model = services
        fields = '__all__'