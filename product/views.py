from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View


# Create your views here.
class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 2
    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'pro'
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        loaded_object = self.object # getting the product ID
        favorite_products = self.request.session.get('favorite') # fetching the favorit IDs
        if str(loaded_object.id) in favorite_products: # if the product was in the favorite items
            context['favorite_products'] = True
        return context

class AddProductFavorite(View):
        def post(self, request):
            product_id = request.POST.get('productID')
            favorite = request.session.get('favorite', [])
            if product_id not in favorite:
                favorite.append(product_id)
                request.session['favorite'] = favorite
            product = Product.objects.get(pk=product_id)
            return redirect(product.get_absolute_url())



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

