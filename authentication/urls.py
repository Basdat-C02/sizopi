from django.urls import path
from .views import home_view, login_view, choose_role_view, register_view

app_name = 'authentication'

urlpatterns = [
    path('', home_view, name='home'),
    path('auth/login/', login_view, name='login'),
    path('auth/choose-role/', choose_role_view, name='choose_role'),
    path('auth/register/', register_view, name='register'),
]
