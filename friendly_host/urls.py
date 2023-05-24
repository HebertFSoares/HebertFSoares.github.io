from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include("usuarios.urls")),
    path('home/', include("home.urls"))
]
