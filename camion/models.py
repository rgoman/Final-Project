from django.db import models

# Create your models here.
from django.db import models
#from trainer.models import Trainer


class Camion(models.Model):

    # gender_options = (
    #     ('male', 'Male'),
    #     ('female', 'Female')
    # )

    numar_inmatriculare = models.CharField(max_length=10)
    serie_sasiu = models.CharField(max_length=17)
    kilometraj_actual = models.IntegerField()
    #email = models.EmailField(max_length=50)
    #description = models.TextField(max_length=500)
    prima_inmatriculare = models.DateField()
    ITP_valabil_pana_la = models.DateField()
    # active = models.BooleanField(default=True)
    # gender = models.CharField(choices=gender_options,max_length=6)
    # trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    # profile = models.ImageField(upload_to='profiles/', null=True)

    #profile = models.FileField

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #auto_now_add - folosti pt a stoca data si ora la momentul introducerii. Nu se mai modifica
    #auto_now - folosit pentru a stoca data si ora de fiecare data cand se modifica date pe inregistrare.

    def __str__(self):
        return f'{self.numar_inmatriculare} {self.serie_sasiu} {self.ITP_valabil_pana_la}'