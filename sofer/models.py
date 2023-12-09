from django.db import models
from camion.models import Camion


class Sofer(models.Model):

    gender_options = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    age = models.IntegerField()
    # email = models.EmailField(max_length=50)
    # description = models.TextField(max_length=500)
    start_date = models.DateField()
    #end_date = models.DateField()
    #active = models.BooleanField(default=True)
    gender = models.CharField(choices=gender_options,max_length=6)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to='profiles/', null=True)

    #profile = models.FileField

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #auto_now_add - folosti pt a stoca data si ora la momentul introducerii. Nu se mai modifica
    #auto_now - folosit pentru a stoca data si ora de fiecare data cand se modifica date pe inregistrare.

    def __str__(self):
        return f'{self.first_name} {self.last_name} '