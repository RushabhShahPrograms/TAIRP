from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
    path("clear_responses/", views.clear_responses, name="clear_responses"),
]
