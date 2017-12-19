from django.conf.urls import url, include
from main import views

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    url(r'^(?P<category_id>\w+)', views.category, name="category"),
    #url(r'^about/$', views.about, name='about'),
]