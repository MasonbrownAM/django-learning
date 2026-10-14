from django.contrib import admin
from .models import SiteSettings,FooterLink,FooterLinkBox, Slider
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'url')
    list_editable = ('title', 'is_active', 'url')
# Register your models here.
admin.site.register(SiteSettings)
admin.site.register(FooterLink)
admin.site.register(FooterLinkBox)
admin.site.register(Slider, SliderAdmin)