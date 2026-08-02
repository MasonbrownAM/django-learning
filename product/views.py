from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import TemplateView, ListView,DetailView


# Create your views here.
class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'pro'

# class ProductListView(TemplateView):
#     template_name = 'product/product_list.html'
#     def get_context_data(self, **kwargs):
#         products = Product.objects.all()[:5]
#         context = super(ProductListView, self).get_context_data(**kwargs)
#         context['products'] = products
#         return context


# class ProductDetailView(TemplateView):
#     template_name = 'product/product_detail.html'
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(**kwargs)
#         slug = self.kwargs['slug']
#         products = get_object_or_404(Product, slug=slug)
#         context['pro'] = products
#         return context

