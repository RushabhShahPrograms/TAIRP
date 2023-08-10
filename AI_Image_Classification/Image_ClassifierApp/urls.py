<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('predict/', views.PredictView.as_view(), name='predict'),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('predict/', views.PredictView.as_view(), name='predict'),
>>>>>>> 0fb0c66000e07c1d11087329b62690269a8180e7
]