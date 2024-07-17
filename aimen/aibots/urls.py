from django.urls import path, include
from . import views

app_name = 'aibots'

urlpatterns = [
    path('', views.index, name='home'),
]
