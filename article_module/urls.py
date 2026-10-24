from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles'),
    path('cat/<str:category_name>/', views.ArticlesView.as_view(), name='articles_by_category_list'),
    path('<int:pk>/<str:title>/', views.ArticleDetailView.as_view(), name='article_detail'),

]