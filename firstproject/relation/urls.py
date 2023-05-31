from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('voiture/', views.all_voiture),
    path('marque/', views.all_marque),
    path('add_voiture/', views.ajout_voiture),
    path('add_marque/', views.ajout_marque),
    path('traitement/<int:id>/', views.traitement), # type: ignore
    path('delete_auto/<int:id>/', views.delete_auto),
    path('delete_marque/<int:id>/', views.delete_marque),
    path('update_auto/<int:id>/',views.update_auto),
    path('update_marque/<int:id>/', views.update_marque),
    path('view_auto/<int:id>/', views.view_auto),
    path('view_marque/<int:id>/',views.view_marque),
]