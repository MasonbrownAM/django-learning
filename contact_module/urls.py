from django.urls import path
from . import views
urlpatterns = [
    # path('', views.contact_us, name='contact_module'),
    path('', views.ContactForm.as_view(), name='contact_module'),
    path('create-profile/', views.CreateProfileView.as_view(), name='create_profile'),

]