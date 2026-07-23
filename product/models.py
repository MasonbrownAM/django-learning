from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class ProductsCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='title in url', db_index=True)
    is_active = models.BooleanField(verbose_name='is active?')
    is_delete = models.BooleanField(verbose_name='حذف شده است؟')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    is_active = models.BooleanField(verbose_name='is active?')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

class Product(models.Model):
    titel = models.CharField(max_length=300, db_index=True)
    category = models.ManyToManyField(ProductsCategory, related_name='products_category', verbose_name='کتگوری')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    short_desc = models.TextField(max_length=360, null=True, blank=True, verbose_name='توضیحات اصلی')
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False, db_index=True, max_length=200, unique=True, blank=True)
    is_delete = models.BooleanField(verbose_name='حذف شده است؟')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', blank=True, null=True )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titel)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.titel}, {self.price}'

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.slug])

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, verbose_name='کپشن', db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags', verbose_name='محصول')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

