from django.urls import path
from . import views

app_name = 'ImageClassifierApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('classify/', views.image_classification, name='image_classification'),
]
