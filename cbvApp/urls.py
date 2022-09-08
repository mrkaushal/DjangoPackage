from django.urls import path
from cbvApp import views

app_name = 'cbvApp'

urlpatterns = [
    path('create', views.UserCreateView.as_view(), name='create'),
    path('list', views.UserListView.as_view(), name='list'),
    path('detail/<int:pk>', views.UserDetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.UserDeleteView.as_view(), name='delete'),
]
