from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from sofer.forms import SoferForm
from sofer.models import Sofer


# CreateView este o clasa dezvoltata de django care ne ajuta sa definim un obiect in baza de date si afisarea unui formular asociat modelului diferit.

#principalele caracteristici:

# Formular de creare: Automat se genereaza un Formular asociat modelului pentru a adauga un obiect nou
# Proesarea datelor: gestionarea procesarea datelor introduse in formular prin validare
# redirect dupa creare : in momentul in care obiectul este creat, poate sa fie redirectionat pe pagina dorita de noi.
#

class SoferCreateView(CreateView):
    template_name = 'sofer/adaugare_sofer.html'
    model = Sofer
    form_class = SoferForm
    #fields = '__all__' # in formular se vor regasi toate fieldurile
    success_url = reverse_lazy('home')
    # permission_required = 'student.add_student'

# # LISTVIEW: este o clasa dezvoltaa de Django care va ajuta pentru afisarea unei liste de obiecte dintr-un model in template
#
# # Principale caracteristici:
#
# # Gestionarea listei: automatizeaza procesul de preluare a listei de obiecte dintr-un model.
# # Sablon/tEMPLATE implici: ListView foloseste un sablon implicit dar el va va lasa sa il folositi pe al vostru (model_list.html)
#
class SoferListView(ListView):
    template_name = 'sofer/lista_soferi.html'
    model = Sofer
    context_object_name = 'toti_soferii'
    # permission_required = 'student.view_list_of_students'
# # UpdateView este o clasa generica din Django  care este utilizata pentru a afisa un formular cu scopul de a actualiza
# # informatiile despre obiectul existent din baza de date.
#
# class StudentUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'student/update_student.html'
#     model = Student
#     form_class = StudentUpdateForm
#     success_url = reverse_lazy('list-of-students')
#
# #DeleteView este o clasa generica din Django care este utilizata pentru a sterge un obiect din baza de date
# #o clasa generica reprezinta o clasa care este definita cu parametri de tipuri variabile
# #care permit ca aceeasi clasa sa fie utilizata pentru diferite tipuri de date
# #oferind flexibilitate si reutilizare cod.
# #beneficiile utilizarii:
# #1. reducerea repetitiilor
# #2. utilizarea principiilor DRY (Don`t repeat yourself!)
#     #2.1. redundanta este evitarea duplicarii de cod in diferite parti ale unei aplicatii.
#     #2.2. refolosirea codului
#     #2.3. mentinerea coerentei si a coeziunii
#
#
# class StudentDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = 'student/delete_student.html'
#     model = Student
#     success_url = reverse_lazy('list-of-students')
#
#
# # DetailView -> este o clasa generica in Django care este utilizata pentru a afisa detaliile unui singur obiect dintr-un
# # model.
#
# class StudentDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'student/details_student.html'
#     model = Student
