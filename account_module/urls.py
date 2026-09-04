from django.urls import path
from account_module import views
urlpatterns = [
    path('sign-in/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('activate-account/<email_active_code>', views.ActivateView.as_view(), name='activate'),
]