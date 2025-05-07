from django.urls import path
from .views import * 

app_name = 'authentication'

urlpatterns = [
    path('', landing_view, name='landing'),
    path('auth/login/', login_view, name='login'),
    path('auth/choose-role/', choose_role_view, name='choose_role'),
    path('auth/register-pengunjung/', register_pengunjung_view, name='register_pengunjung'),
    path('auth/register-dokter-hewan/', register_dokter_hewan_view, name='register_dokter_hewan'),
    path('auth/register-staff/', register_staff_view, name='register_staff'),
    
    path('profile/profile-pengguna/', profile_view, name='profile_pengguna'),
]
