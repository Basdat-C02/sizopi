from django.urls import path
from . import views

app_name = 'adopsi'

urlpatterns = [
    #staff
    path('adopsi/status-adopsi/', views.status_adopsi, name='status_adopsi'),
    path('adopsi/form-adopsi/<uuid:hewan_id>/', views.form_adopsi, name='form_adopsi'),
    path('adopsi/verifikasi-adopter/<uuid:hewan_id>/', views.verifikasi_adopter, name='verifikasi_adopter'),
    path('adopsi/submit-adopsi-individu/<uuid:hewan_id>/', views.submit_adopsi_individu, name='submit_adopsi_individu'),
    path('adopsi/submit-adopsi-organisasi/<uuid:hewan_id>/', views.submit_adopsi_organisasi, name='submit_adopsi_organisasi'),
    path('adopsi/update-status-adopsi/<uuid:hewan_id>/', views.update_status_adopsi, name='update_status_adopsi'),
    path('adopsi/hentikan-adopsi/<uuid:hewan_id>/', views.hentikan_adopsi, name='hentikan_adopsi'),
    path('adopsi/hentikan-adopsi-user/<uuid:hewan_id>/', views.hentikan_adopsi_user, name='hentikan_adopsi_user'),
    #riwayat adopsi
    path('adopsi/daftar-adopter/', views.daftar_adopter, name='daftar_adopter'),
    path('adopsi/riwayat-adopsi/<uuid:adopter_id>/', views.riwayat_adopsi, name='riwayat_adopsi'),
    path('adopsi/hapus-adopter/<uuid:adopter_id>/', views.hapus_adopter, name='hapus_adopter'),
    path('adopsi/hapus-adopsi/<uuid:adopsi_id>/', views.hapus_adopsi, name='hapus_adopsi'),

    #user
    path('adopsi/adopsi-saya/', views.adopsi_saya, name='adopsi_saya'),
    path('adopsi/sertifikat/<uuid:hewan_id>/', views.lihat_sertifikat, name='lihat_sertifikat'),
    path('adopsi/kondisi/<uuid:hewan_id>/', views.pantau_kondisi, name='pantau_kondisi'),
    path('adopsi/perpanjang/<uuid:hewan_id>/', views.perpanjang_adopsi, name='perpanjang_adopsi'),
    path('adopsi/hentikan-adopsi-user/<uuid:hewan_id>/', views.hentikan_adopsi_user, name='hentikan_adopsi_user'),
]