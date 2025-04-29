from django.urls import path
from .views import *

app_name = 'hiburan'

urlpatterns = [
    path('', fasilitas_menu, name='fasilitas_menu'),

    # atraksi
    path('atraksi', data_atraksi_view, name='data_atraksi'),
    path('atraksi/create', create_atraksi_view, name='create_atraksi'),
    path('atraksi/edit/<str:nama>', edit_atraksi_view, name='edit_atraksi'),
    path('atraksi/delete/<str:nama>', delete_atraksi_view, name='delete_atraksi'),

    # wahana
    path('wahana', data_wahana_view, name='data_wahana'),
    path('wahana/create', create_wahana_view, name='create_wahana'),
    path('wahana/edit/<str:nama>', edit_wahana_view, name='edit_wahana'),
    path('wahana/delete/<str:nama>', delete_wahana_view, name='delete_wahana'),

    # reservasi
    path('reservasi', data_reservasi_view, name='data_reservasi'),
    path('reservasi/create', create_reservasi_view, name='create_reservasi'),
    path('reservasi/detail/<str:id>', detail_reservasi_view, name='detail_reservasi'),
    path('reservasi/edit/<str:nama>', edit_reservasi_view, name='edit_reservasi'),
    path('reservasi/delete/<str:nama>', delete_reservasi_view, name='delete_reservasi'),
]