from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This can be your home page or a landing page
    path('digit_recognition/', views.digit_recognition, name='digit_recognition'),
]
