from django.urls import path
from .views import rekam_medis_hewan, list_rekam_medis, edit_rekam_medis, create_rekam_medis

app_name='kesehatan'

urlpatterns = [
    path('list-rekam-medis/', list_rekam_medis, name='list_rekam_medis'),
    path('rekam_medis_hewan/<uuid:pk>/', rekam_medis_hewan, name='rekam_medis_hewan'),
    path('edit-rekam-medis/<uuid:pk>/', edit_rekam_medis, name='edit_rekam_medis'),
    path('delete-rekam-medis/<uuid:pk>/', rekam_medis_hewan, name='delete_rekam_medis'),
    path('create-rekam-medis/<uuid:pk>', create_rekam_medis, name='create_rekam_medis'),
]