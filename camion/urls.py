from django.urls import path

from camion import views

urlpatterns = [
     path('adaugare_camion/', views.CamionCreateView.as_view(), name = 'adaugare-camion'),
     path('lista_camioane/', views.CamionListView.as_view(), name = 'lista-camioane'),
    # path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name = 'update-student'),
     path('stergere_camion/<int:pk>/', views.CamionDeleteView.as_view(), name = 'stergere-camion'),
    # path('detail_student/<int:pk>/', views.StudentDetailView.as_view(), name = 'detail-student'),
]