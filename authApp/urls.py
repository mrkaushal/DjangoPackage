from django.urls import path
from authApp import views

app_name = 'authApp'

urlpatterns = [
    path('', views.AuthLoginView.as_view(), name='login'),
    path('signout', views.AuthLogoutView.as_view(), name='logout'),
]
