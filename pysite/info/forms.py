from .models import Info
from django.forms import ModelForm ,TextInput, DateTimeInput
from django import forms

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'anons', 'date']
        
        widgets = {
            "title":TextInput(attrs={
                'class':'form_control',
                'placeholder':'Name'
            } ),
            "anons":TextInput(attrs={
                'class':'form_control',
                'placeholder':'Info'
            } ),
            "date":DateTimeInput(attrs={
                'class':'form_control',
                'placeholder':'Date'
            } )
        }