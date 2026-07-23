from django.contrib import admin
from .models import ContactUs
# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    name = 'Contact Us'
    verbose_name = 'تماس با ما'
    list_display = ['name', 'title']

admin.site.register(ContactUs, ContactUsAdmin)