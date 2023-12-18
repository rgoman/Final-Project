from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from sofer.models import Sofer


class SoferForm(forms.ModelForm):
    class Meta:
        model = Sofer
        fields = '__all__'  # in formular se vor regasi toate fieldurile in ordinea definita in models.py

        widgets ={
            'prenume': TextInput(attrs={'class': 'form-control','placeholder': 'Please enter your first name'}),
            'nume': TextInput(attrs={'class': 'form-control','placeholder': 'Please enter your last name'}),
            'numar_de_telefon': NumberInput(attrs={'class': 'form-control','placeholder': 'Please enter your phone number'}),
            'varsta': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            # 'email': EmailInput(attrs={'class': 'form-control','placeholder': 'Please enter your email'}),
            # 'description': Textarea(attrs={'class': 'form-control','placeholder': 'Please enter your description', 'rows': 3}),
            'data_incepere': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'camion': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data  # veti sctoca un dict cu valorile completate de utilizator in formular
    #
    #     # Unicitate pe adresa de email
    #     get_email = cleaned_data['email']  # cleaned_data.get('email') ACCESAM VALOAREA INTRODUSA DE UTILIZATOR
    #     check_emails = Student.objects.filter(
    #         email=get_email)  # CAUTAM VALOAREA INTRODUSA DE UTILIZATOR IN TABELA PE COLOANA EMAIL
    #     if check_emails:  # DACA EXISTA CEL PUTIN UN STUDENT CU ACEEASI ADRESA DE EMAIL
    #         msg = 'Exista un student cu aceasta adresa de email'  # GENEREAM MESAJUL PENTRU AFISARE
    #         self._errors['email'] = self.error_class([msg])  # LOCALIZAM PE CEL FIELD VREM SA AFISAM MESAJUL ERORII
    #
    #     # Validare pentru start_date si end_date. Daca start_date > end_date atunci sa ii afisam o eroare
    #     get_start_date = cleaned_data['start_date']
    #     get_end_date = cleaned_data['end_date']
    #
    #     if get_start_date > get_end_date:
    #         msg_start_end = 'Data de incepere este mai mare decat data incheierii. Va rugam sa revizuiti data introdusa.'
    #         self._errors['end_date'] = self.error_class([msg_start_end])
    #
    #     # O unicitate pe first_name si last_name. Nu trebuie sa existe un alt student cu acelasi first_name si last_name
    #     get_first_name = cleaned_data['first_name']
    #     get_last_name = cleaned_data['last_name']
    #     check_first_last_name = Student.objects.filter(first_name=get_first_name, last_name=get_last_name)
    #
    #     if check_first_last_name :
    #         msg_names = 'Acest cursant este deja inregistrat.'
    #         self._errors['last_name'] = self.error_class([msg_names])
    #
    #     # O validare pe description, sa nu poata adauga un text mai mare de 50 de caractere
    #     get_description = cleaned_data['description']
    #     if len(get_description) > 50 :
    #         msg_description = 'Prea multe povesti. Va rugam sa fiti mai concret.'
    #         self.errors['description'] = self.error_class([msg_description])
    #     # O validare daca first_name < 3 si last_name < 3
    #     if len(get_first_name) < 3:
    #         msg_len_names = 'Acest nume nu este valid'
    #         self.errors['first_name'] = self.error_class([msg_len_names])
    #     if len(get_last_name) < 3:
    #         msg_len_names = 'Acest nume nu este valid'
    #         self.errors['last_name'] = self.error_class([msg_len_names])
    #
        return cleaned_data

# class StudentUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'  # in formular se vor regasi toate fieldurile in ordinea definita in models.py
#
#         widgets ={
#             'first_name': TextInput(attrs={'class': 'form-control','placeholder': 'Please enter your first name'}),
#             'last_name': TextInput(attrs={'class': 'form-control','placeholder': 'Please enter your last name'}),
#             'age': NumberInput(attrs={'class': 'form-control','placeholder': 'Please enter your age'}),
#             'email': EmailInput(attrs={'class': 'form-control','placeholder': 'Please enter your email'}),
#             'description': Textarea(attrs={'class': 'form-control','placeholder': 'Please enter your description', 'rows': 3}),
#             'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'gender': Select(attrs={'class': 'form-select'}),
#             'trainer': Select(attrs={'class': 'form-select'}),
#         }
