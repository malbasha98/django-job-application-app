from django.urls import path
from . import views

# Use the exact variable name here!!!
urlpatterns = [
    path('', views.index, name="index")
]