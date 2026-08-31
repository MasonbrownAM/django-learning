from django.urls import path
from account_module import views
urlpatterns = [
    path('sign-in/', views.RegisterView.as_view(), name='register'),
]