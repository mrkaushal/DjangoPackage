from django.urls import path
from authApp import views

app_name = 'authApp'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
]
