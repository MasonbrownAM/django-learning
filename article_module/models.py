from django.db import models

# Create your models here.

class ArticleCathegory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    parent = models.ForeignKey('ArticleCathegory', on_delete=models.CASCADE, verbose_name='دسته بندی والد', blank=True, null=True)
    url_title = models.CharField(max_length=200, unique=True)
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'دسته بندی مقالات'
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    content = models.TextField()
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, allow_unicode=True, verbose_name='عنوان در url', blank=True, null=True)
    image = models.ImageField(upload_to='images/article_images', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    cathegory = models.ManyToManyField('ArticleCathegory', blank=True)
    class Meta:
        verbose_name = ' مقاله'
        verbose_name_plural = 'مقالات'
    def __str__(self):
        return self.title