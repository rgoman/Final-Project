from django.urls import path

from camion import views

urlpatterns = [
     path('add_truck/', views.CamionCreateView.as_view(), name = 'add-truck'),
    # path('list_of_students/', views.StudentListView.as_view(), name = 'list-of-students'),
    # path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name = 'update-student'),
    # path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name = 'delete-student'),
    # path('detail_student/<int:pk>/', views.StudentDetailView.as_view(), name = 'detail-student'),
]