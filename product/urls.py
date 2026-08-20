from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('favorite/', views.AddProductFavorite.as_view(), name='favorite'),
]