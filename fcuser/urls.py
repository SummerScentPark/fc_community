from django.urls import path
from . import views
from fcuser.views import home

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('', home),
]
