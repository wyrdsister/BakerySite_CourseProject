from django.urls import path
from django.conf.urls import url, include
from main import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]