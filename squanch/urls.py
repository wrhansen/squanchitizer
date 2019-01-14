from django.urls import path

from . import views

urlpatterns = [
    path('', views.squanch, name='index'),
    path('squanchitize', views.squanchitize, name='squanchitize')
]
