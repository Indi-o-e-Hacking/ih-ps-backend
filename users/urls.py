from django.urls import path
from .views import UserRegistrationView, UserListView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='user-register'),
    path('', UserListView.as_view(), name='user-list'),
] 