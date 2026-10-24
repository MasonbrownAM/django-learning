from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, ArticleCathegory
from jalali_date import datetime2jalali
# Create your views here.
class ArticlesView(ListView):
    template_name = 'article_module/article.html'
    model = Article
    paginate_by = 1
    context_object_name = 'articles'

    def get_context_data(self,*args, **kwargs):
        context = super(ArticlesView, self).get_context_data(**kwargs)
        return context
    def get_queryset(self):
        queryset = super(ArticlesView, self).get_queryset()
        queryset = queryset.filter(is_active=True)
        category_name = self.kwargs.get('category_name')
        if category_name:
            queryset = queryset.filter(category__url_title__iexact=category_name)
        return queryset

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail.html'
    def get_queryset(self):
        queryset = super(ArticleDetailView, self).get_queryset()
        query = queryset.filter(is_active=True)
        return query


def article_categories_partial(request):
    article_main_category = ArticleCathegory.objects.filter(is_active=True,parent_id=None)
    context = {
        'main_category':article_main_category,
    }
    return render(request,'article_module/includes/article_cathgories_component.html',context)