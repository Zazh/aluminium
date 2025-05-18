# contents/urls.py
from django.urls import path
from .views import home_view

app_name = "contents"

urlpatterns = [
    path("", home_view, name="home"),
]