from django.urls import path
from .views import *

app_name = 'hiburan'

urlpatterns = [
    # atraksi
    path('fasilitas/atraksi', data_atraksi_view, name='data_atraksi'),
    path('fasilitas/atraksi/create', create_atraksi_view, name='create_atraksi'),
    path('fasilitas/atraksi/edit/<str:nama>', edit_atraksi_view, name='edit_atraksi'),
    path('fasilitas/atraksi/delete/<str:nama>', delete_atraksi_view, name='delete_atraksi'),

    # wahana
    path('fasilitas/wahana', data_wahana_view, name='data_wahana'),
    path('fasilitas/wahana/create', create_wahana_view, name='create_wahana'),
    path('fasilitas/wahana/edit/<str:nama>', edit_wahana_view, name='edit_wahana'),
    path('fasilitas/wahana/delete/<str:nama>', delete_wahana_view, name='delete_wahana'),

    # reservasi
    path('fasilitas/reservasi', data_reservasi_view, name='data_reservasi'),
    path('fasilitas/reservasi/create', create_reservasi_view, name='create_reservasi'),
    path('fasilitas/reservasi/edit/<str:nama>', edit_reservasi_view, name='edit_reservasi'),
    path('fasilitas/reservasi/delete/<str:nama>', delete_reservasi_view, name='delete_reservasi'),
]