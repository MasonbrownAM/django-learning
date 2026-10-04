from django.db import models

# Create your models here.
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    about_us_text = models.TextField(verbose_name='درباره سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, verbose_name='تلفن', null=True, blank=True)
    email = models.EmailField( verbose_name='ایمیل', null=True, blank=True)
    copyright= models.TextField(max_length=200, verbose_name='کپی رایت')
    site_logo= models.ImageField(upload_to='images/site_settings', verbose_name='لوگوی سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات'

    def __str__(self):
        return self.site_name

class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'link box'
    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    footer_link_box = models.ForeignKey(FooterLinkBox, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'link'
    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description =  models.TextField(max_length=200, verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(upload_to='images/sliders', null=True, blank=True, verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال', default=True, blank=True,null=True)
    class Meta:
        verbose_name = 'اسلایدر'

    def __str__(self):
        return self.title