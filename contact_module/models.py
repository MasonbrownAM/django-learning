from django.db import models
# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    email = models.EmailField(verbose_name='email')
    title  = models.CharField(max_length=300, verbose_name='موضوع' )
    description = models.TextField(verbose_name='توضیحات')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده')
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'
        ordering = ('name',)
    def __str__(self):
        return f'{self.name}--{self.title}'