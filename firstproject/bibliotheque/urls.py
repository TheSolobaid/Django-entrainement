from django.urls import path
from . import views

urlpatterns = [
    path('ajout', views.ajout),
    path('traitement', views.traitement),
    path('traitement/', views.traitement),
    path('all/', views.all, name='all'),
    path('affiche', views.affiche),
]