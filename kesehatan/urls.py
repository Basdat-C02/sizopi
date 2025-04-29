from django.urls import path
from .views import rekam_medis_hewan, list_rekam_medis, edit_rekam_medis, create_rekam_medis, delete_rekam_medis, jadwal_pemeriksaan, create_jadwal_pemeriksaan, edit_jadwal_pemeriksaan, delete_jadwal_pemeriksaan, edit_freq_pemeriksaan, pemberian_pakan, create_pemberian_pakan, update_pemberian_pakan, delete_pemberian_pakan, riwayat_pemberian_pakan

app_name='kesehatan'

urlpatterns = [
    path('list-rekam-medis/', list_rekam_medis, name='list_rekam_medis'),
    path('rekam_medis_hewan/<uuid:pk>/', rekam_medis_hewan, name='rekam_medis_hewan'),
    path('edit-rekam-medis/<uuid:pk>/', edit_rekam_medis, name='edit_rekam_medis'),
    path('delete-rekam-medis/<uuid:pk>/', rekam_medis_hewan, name='delete_rekam_medis'),
    path('create-rekam-medis/<uuid:pk>', create_rekam_medis, name='create_rekam_medis'),
    path('delete-rekam-medis/<uuid:pk>/', delete_rekam_medis, name='delete_rekam_medis'),
    path('jadwal-pemeriksaan/<uuid:pk>/', jadwal_pemeriksaan, name='jadwal_pemeriksaan'),
    path('create-jadwal-pemeriksaan/<uuid:pk>/', create_jadwal_pemeriksaan, name='create_jadwal_pemeriksaan'),
    path('edit-jadwal-pemeriksaan/<uuid:pk>/', edit_jadwal_pemeriksaan, name='edit_jadwal_pemeriksaan'),
    path('delete-jadwal-pemeriksaan/<uuid:pk>/', delete_jadwal_pemeriksaan, name='delete_jadwal_pemeriksaan'),
    path('edit-freq-pemeriksaan/<uuid:pk>/', edit_freq_pemeriksaan, name='edit_freq_pemeriksaan'),
    path('pemberian-pakan/<uuid:pk>/', pemberian_pakan, name='pemberian_pakan'),
    path('create-pemberian-pakan/<uuid:pk>', create_pemberian_pakan, name='create_pemberian_pakan'),
    path('update-pemberian-pakan/<uuid:pk>', update_pemberian_pakan, name='update_pemberian_pakan'),
    path('delete-pemberian-pakan/<uuid:pk>', delete_pemberian_pakan, name='delete_pemberian_pakan'),
    path('beri-pakan/<uuid:pk>/', pemberian_pakan, name='beri_pakan'),
    path('riwayat-pemberian-pakan/', riwayat_pemberian_pakan, name='riwayat_pemberian_pakan'),
]