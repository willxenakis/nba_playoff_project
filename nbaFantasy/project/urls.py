from django.urls import path

from . import views

urlpatterns = [
    path('', views.predictions, name='predictions'),
    path('submit', views.stats, name='submit'),
    path('predictions', views.predictions, name='home'),
    path('stats', views.defaultStats, name='stats'),
    path('specificStats', views.specificStats, name='specificStats'),
]