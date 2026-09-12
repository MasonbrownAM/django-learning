from django.urls import path
from account_module import views
urlpatterns = [
    path('sign-in/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('activate-account/<email_active_code>', views.ActivateView.as_view(), name='activate'),
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget-password'),
    path('reset-password/<active_code>', views.ResetPasswordView.as_view(), name='reset-password'),

]