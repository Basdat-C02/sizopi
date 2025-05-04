from django.urls import path
from .views import home_view, login_view, choose_role_view, register_dokter_hewan_view, register_pengunjung_view, register_staff_view

app_name = 'authentication'

urlpatterns = [
    path('', home_view, name='landing'),
    path('auth/login/', login_view, name='login'),
    path('auth/choose-role/', choose_role_view, name='choose_role'),
    path('auth/register-pengunjung/', register_pengunjung_view, name='register_pengunjung'),
    path('auth/register-dokter-hewan/', register_dokter_hewan_view, name='register_dokter_hewan'),
    path('auth/register-staff/', register_staff_view, name='register_staff'),
]
