from django.urls import path
from .views import *

app_name = 'authentication'

urlpatterns = [
    path('', home_view, name='home'),
    path('auth/login/', login_view, name='login'),
    path('auth/choose-role/', choose_role_view, name='choose_role'),
    path('auth/register-pengunjung/', register_pengunjung_view, name='register_pengunjung'),
    path('auth/register-dokter-hewan/', register_dokter_hewan_view, name='register_dokter_hewan'),
    path('auth/register-staff/', register_staff_view, name='register_staff'),
    
    path('profile/profile-pengunjung/', profile_pengunjung_view, name='profile_pengunjung'),
    path('profile/profile-dokter-hewan/', profile_dokter_hewan_view, name='profile_dokter_hewan'),
    path('profile/profile-staff/', profile_staf_admin_view, name='profile_staff'),
    path('profile/profile-pelatih/', profile_pelatih_hewan_view, name='profile_pelatih_hewan'),
    path('profile/profile-penjaga/', profile_penjaga_hewan_view, name='profile_penjaga_hewan'),
    
    path('edit-profile/pengunjung/', edit_profile_pengunjung_view, name='edit_profile_pengunjung'),
    path('edit-profile/dokter-hewan/', edit_profile_dokter_hewan_view, name='edit_profile_dokter_hewan'),
    path('edit-profile/profile-staff/', edit_profile_staff_view, name='edit_profile_staff'),
    path('edit-profile/ubah-password/', ubah_password_view, name='edit_password'),
]
