from django.urls import path

from article_module.views import ArticlesView

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles_list'),
]