from django.conf.urls import url, include
from main import views

urlpatterns = [
    url(r'^(?P<category_id>\w+)', views.category, name="category"),
]