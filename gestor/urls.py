from django.urls import path
from gestor import views

urlpatterns = [
    path("", views.home, name="home"),
]