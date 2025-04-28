from django.urls import path
from habitat.views import daftar_habitat_view

app_name = 'habitat'

urlpatterns = [
    path('habitat/daftar_habitat/', daftar_habitat_view, name='daftar_habitat'),
]