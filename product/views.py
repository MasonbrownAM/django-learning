from django.shortcuts import render, get_object_or_404
from .models import Product,ProductsCategory
from django.db.models import Avg, Min, Max # برای محاصبه در دیتابیس و اجرای آن در تابع Aggregate
# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('price')[:5]# برای اوردر کردن محصولات از تایتل

    total_number_of_products = products.count()# شمارش محصولات
    return render(request, 'product/product_list.html', context={
        'products': products,
        })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', context= {
        'pro':product})
