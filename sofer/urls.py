from django.urls import path

from sofer import views

# from student import views

urlpatterns = [
     path('adaugare_sofer/', views.SoferCreateView.as_view(), name = 'adaugare-sofer'),
     path('lista_soferi/', views.SoferListView.as_view(), name = 'lista-soferi'),
    # path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name = 'update-student'),
    # path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name = 'delete-student'),
    # path('detail_student/<int:pk>/', views.StudentDetailView.as_view(), name = 'detail-student'),
]