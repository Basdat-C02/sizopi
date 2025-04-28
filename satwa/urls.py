from django.urls import path
from satwa.views import add_satwa_view

app_name = 'satwa'

urlpatterns = [
    path('satwa/add_satwa/', add_satwa_view, name='add_satwa'),
]
