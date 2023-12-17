from django import forms
from django.forms import TextInput, EmailInput, Select, NumberInput, Textarea, DateInput

from camion.models import Camion


class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = '__all__'

        widgets ={
            'numar_inmatriculare': TextInput(attrs={'class': 'form-control','placeholder': 'Va rugam sa introduceti numarul de inmatriculare'}),
            'serie_sasiu': TextInput(attrs={'class': 'form-control','placeholder': 'Va rugam sa introduceti seria de sasiu'}),
            'kilometraj_actual': NumberInput(attrs={'class': 'form-control','placeholder': 'Va rugam sa introduceti kilometrajul masinii'}),
            'prima_inmatriculare': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ITP_valabil_pana_la': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            #'asigurare_valabila_pana_la': DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }

# class TrainerUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Trainer
#         fields = '__all__'
#
#         widgets = {
#             'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Pleas enter your first name'}),
#             'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Pleas enter your last name'}),
#             'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the course name'}),
#             'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Pleas enter your e-mail address'}),
#             'departament': Select(attrs={'class': 'form-select'}),
#         }