from django.urls import path
from habitat.views import daftar_habitat_view, add_habitat_view, edit_habitat_view, detail_habitat_view

app_name = 'habitat'

urlpatterns = [
    path('habitat/daftar_habitat/', daftar_habitat_view, name='daftar_habitat'),
    path('habitat/add_habitat/', add_habitat_view, name='add_habitat'),
    path('habitat/edit_habitat/', edit_habitat_view, name='edit_habitat'),
    path('habitat/detail_habitat/', detail_habitat_view, name='detail_habitat'),
]