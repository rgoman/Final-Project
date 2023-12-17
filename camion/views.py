from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from camion.forms import CamionForm
from camion.models import Camion


# from trainer.forms import TrainerForm, TrainerUpdateForm
# from trainer.models import Trainer


# CreateView este o clasa dezvoltata de django care ne ajuta sa definim un obiect in baza de date si afisarea unui formular asociat modelului diferit.

#principalele caracteristici:

# Formular de creare: Automat se genereaza un Formular asociat modelului pentru a adauga un obiect nou
# Proesarea datelor: gestionarea procesarea datelor introduse in formular prin validare
# redirect dupa creare : in momentul in care obiectul este creat, poate sa fie redirectionat pe pagina dorita de noi.
#



class CamionCreateView(CreateView):
    template_name = 'camion/add_truck.html'
    model = Camion
    form_class = CamionForm
    success_url = reverse_lazy('home')

# class TrainerListView(LoginRequiredMixin, ListView):
#     template_name = 'trainer/list_of_trainers.html'
#     model = Trainer
#     context_object_name = 'all_trainers'
#
# class TrainerUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'trainer/update_trainer.html'
#     model = Trainer
#     form_class = TrainerUpdateForm
#     success_url = reverse_lazy('list-of-trainers')
#
# class TrainerDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = 'trainer/delete_trainer.html'
#     model = Trainer
#     success_url = reverse_lazy('list-of-trainers')
# @login_required()
# def activate_trainer(request, pk):
#     Trainer.objects.filter(id=pk).update(active=True)
#     return redirect('list-of-trainers')
#
# @login_required()
# def inactivate_trainer(request, pk):
#     Trainer.objects.filter(id=pk).update(active=False)
#     return redirect('list-of-trainers')
#
# class TrainerDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'trainer/details_trainer.html'
#     model = Trainer