from django.urls import path
from adopsi import views

app_name = 'adoption'
urlpatterns = [
    path('', views.main_staff, name='main_staff'),
    path('adopter/', views.main_adopter, name='main_adopter'),
    path('detail/<uuid:animal_id>/', views.detail_modal, name='detail_modal'),
    path('register/', views.register_adopter, name='register_adopter'),
    path('history/', views.adopter_history, name='adopter_history'),
    path('certificate/<uuid:animal_id>/', views.certificate, name='certificate'),
    path('extend/<uuid:animal_id>/', views.extend_adoption, name='extend_adoption'),
]