from django.urls import path
from satwa.views import add_satwa_view, daftar_satwa_view, edit_satwa_view

app_name = 'satwa'

urlpatterns = [
    path('satwa/add_satwa/', add_satwa_view, name='add_satwa'),
    path('satwa/daftar_satwa/', daftar_satwa_view, name='daftar_satwa'),
    path('satwa/edit_satwa/', edit_satwa_view, name='edit_satwa'),
]
