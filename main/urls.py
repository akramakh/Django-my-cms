
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('mail', views.send_mail, name="mail"),
]
