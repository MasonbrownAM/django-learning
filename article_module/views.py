from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

# Create your views here.
class ArticlesView(ListView):
    template_name = 'article_module/article.html'
    model = Article
    paginate_by = 5
    context_object_name = 'articles'