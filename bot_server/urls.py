from django.urls import path
from . import views

urlpatterns = [
    path('', views.execute),
    path('data/', views.index)
]