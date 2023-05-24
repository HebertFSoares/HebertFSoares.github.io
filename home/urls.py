from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('estudante/', views.home_estudante, name="home_estudante"),
    path('anfitriao/', views.home_anfitriao, name='home_anfitriao'),
    path('error/', views.error, name="error"),
    path('adicionar_vaga/', views.AdicionarVagaView.as_view(), name="adicionar_vaga"),
]
